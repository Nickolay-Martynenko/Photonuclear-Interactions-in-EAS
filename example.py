from awkward import from_parquet

HadCascade = from_parquet("./Monte-Carlo/HadCascade.parquet")
print(HadCascade.type)

ElmCascade = from_parquet("./Monte-Carlo/ElmCascade.parquet")
print(ElmCascade.type)
