# Outline of the Analysis (Pseudo-Code)

def HadCascadeFittingPipeline(HadCascade)->bool:
    # see Subsection III A
    PhotonsDistribution = EMPTY
    
    for Event in HadCascade:
        EventContent = EMPTY
        NumPhotons = 0
        for Particle in Event.SecondaryParticles:
            if Particle.ParticleId == 1: # photon
                NumPhotons += 1
                AddPhotons(
                    HowMany=1,
                    Log10Energy=Particle.Log10Energy,
                    SlantDepth=Event.LeadingInteractions[Particle.LeadingInteractionId].SlantDepth,
                    To=EventContent,
                )
            elif Particle.ParticleId == 7: # neutral pion
                NumPhotons += 2
                AddPhotons(
                    HowMany=2,
                    Log10Energy=Particle.Log10Energy - Log10(2),
                    SlantDepth=Event.LeadingInteractions[Particle.LeadingInteractionId].SlantDepth,
                    To=EventContent,
                )
            else:
                pass
        WriteMetadata(
            Fragment=Event.Fragment,
            Log10Energy=Event.Shower_Log10Energy,
            NumPhotons=NumPhotons,
            To=EventContent,
        )
        AddEventContent(EventContent=EventContent, To=PhotonsDistribution)
    
    # see Subsection IV A
    LinRegFit = FitLinearRegression(
        Dataset=PhotonsDistribution,
        Tasks=[
          {
              Target="NumPhotons",        TargetPreproc=lambda Raw: Log(Mean(Raw, GroupBy=Features)),
              Features="Log10Energy",     FeaturePreproc=lambda Raw: Raw + Log(10),
          },
          {
              Target="PhotonLog10Energy", TargetPreproc=lambda Raw: Mean(Raw, GroupBy=Features)+Log(10),
              Features="Log10Energy",     FeaturePreproc=lambda Raw: Raw + Log(10),
          },
          {
              Target="PhotonLog10Energy", TargetPreproc=lambda Raw: StdDev(Raw, GroupBy=Features)+Log(10),
              Features="Log10Energy",     FeaturePreproc=lambda Raw: Raw + Log(10),
          },
          {
              Target="PhotonSlantDepth",  TargetPreproc=lambda Raw: Mean(Raw, GroupBy=Features),
              Features="Log10Energy",     FeaturePreproc=lambda Raw: Raw + Log(10),
          },
        ],
        FilterKey="Fragment", FilterInclude="train",
    )
    
    NormalizedPhotonsDistribution = MakeNormalizedDistribution(
        Dataset=PhotonsDistribution,
        GetParametersFrom=LinRegFit,
    )
    
    MaximumLikelihoodFit = FitMaximumLikelihood(
        Dataset=NormalizedPhotonsDistribution,
        Model=Eq16, Method="COBYQA",
        FilterKey="Fragment", FilterInclude="train",
    )
    
    SaveParameters(From=[LinRegFit, MaximumLikelihoodFit], To="HadCascadeOutput.dat")

    return True
  
def ElmCascadeFittingPipeline(ElmCascade)->bool:
    # see Subsection III B
    MuonDataset = EMPTY
    
    for Event in ElmCascade:
        EventContent = EMPTY
        EventContent.Total = Event.MuonNumber[0, :]
        EventContent.NonPNR = Event.MuonNumber[1, :]
        EventContent.LowEnergyPNR = Event.MuonNumber[2, :] - EventContent.NonPNR
        
        for idx, LeftBinEdge, RightBinEdge in MakeEdgePairs(
                PNR_Log10Energy_BinEdges[3:]
            ):
            EventContent.HighEnergyPNR[idx, :] = Event.MuonNumber[idx, :] - EventContent.NonPNR
            EventContent.PNmu_Density[idx, :] = EventContent.HighEnergyPNR[idx, :] / (RightBinEdge - LeftBinEdge) / Log(10)
            EventContent.PNR_Log10Energy[idx, :] = (RightBinEdge + LeftBinEdge) / 2
                
        print(
            IsClose(
                Sum(EventContent.HighEnergyPNR, Dim=PNR_Log10Energy_Bins) + 
                EventContent.LowEnergyPNR + EventContent.NonPNR, EventContent.Total
            )
        )
        
        WriteMetadata(
            Fragment=Event.Fragment,
            Log10Energy=Event.Shower_Log10Energy,
            SlantDepthProfile=Event.SlantDepth,
            To=EventContent,
        )
        AddEventContent(EventContent=EventContent, To=MuonDataset)

    # see Subsection IV B
    LinRegFit = FitLinearRegression(
        Dataset=MuonDataset,
        Tasks=[
          {
              Target="PNmu_Density",
              TargetPreproc=lambda Raw: Log(Max(Mean(Raw, GroupBy=Features), Dim=Longitudinal)),
              Features=["Log10Energy", "PNR_Log10Energy"],
              FeaturePreproc=lambda Raw: Raw + Log(10),
              FeaturePoly=("x1", "x2", "x2^2"),
          },
          {
              Target=["SlantDepth", "PNmu_Density"], 
              TargetPreproc=lambda Raw: Raw["SlantDepth"][
                        Argmax(Mean(Raw["PNmu_Density"], GroupBy=Features), Dim=Longitudinal)
                  ],
              Features=["Log10Energy", "PNR_Log10Energy"],
              FeaturePreproc=lambda Raw: Raw + Log(10),
          },
          {
              Target=["SlantDepth", "PNmu_Density"],
              TargetPreproc=lambda Raw: (
                  (
                      Raw["SlantDepth"][
                        Argmax(Mean(Raw["PNmu_Density"], GroupBy=Features), Dim=Longitudinal)
                      ] * (
                          1.0 + Log(
                              Raw["SlantDepth"] / 
                              Raw["SlantDepth"][
                                  Argmax(Mean(Raw["PNmu_Density"], GroupBy=Features), Dim=Longitudinal)
                              ]
                          )
                      ) - 
                      Raw["SlantDepth"]
                  ) / (
                      Log(Mean(Raw["PNmu_Density"], GroupBy=Features)) - 
                      Log(Max(Mean(Raw["PNmu_Density"], GroupBy=Features), Dim=Longitudinal))
                  )
              ),
              Features=["PNR_Log10Energy", "xmu"],
              FeaturePreproc=[lambda Raw: Raw + Log(10), None],
              FeaturePoly=("x1", "x2", "x1.x2", "x2^2", "x1.x2^2"),
          },
        ],
        FilterKey="Fragment", FilterInclude="train", FilterOutliers=True
    )
    
    SaveParameters(From=LinRegFit, To="ElmCascadeOutput.dat")

    return True
