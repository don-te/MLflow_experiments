import mlflow

mlflow.set_experiment('YT-MLOPS-Exp2')
df = mlflow.search_runs(experiment_names=['YT-MLOPS-Exp2'])

print(f"Total runs in YT-MLOPS-Exp2: {len(df)}\n")
print("Columns in the dataframe:")
print(df.columns.tolist())
print("\nRun details:")
for idx, row in df.iterrows():
    print(f"\nRun {idx+1}:")
    print(f"  Run ID: {row['run_id']}")
    print(f"  Artifact URI: {row['artifact_uri']}")
