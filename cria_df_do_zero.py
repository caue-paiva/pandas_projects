import pandas as pd
print(pd.__version__)

df = pd.DataFrame()
numero_testes:int  = 1

print(type(df))
df[f"teste_num_{numero_testes}"] = [1,2,3,4]

numero_testes += 1

df[f"teste_num_{numero_testes}"] = [1,22,91,4]

nova_linha : dict = {"teste_num_1":3}

df= pd.concat( [ df, pd.DataFrame([nova_linha]) ], ignore_index=True  )

df.index = ["cria_indv", "evoluiu", "ordenacao", "manda_pygame", "h"]


print(df)


