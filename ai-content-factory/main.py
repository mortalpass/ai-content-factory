from pipelines.content_pipeline import run_pipeline
from storage.saver import save_results
from tqdm import tqdm

def main():
    TOTAL_BATCH = 5
    BATCH_SIZE = 5

    all_results = []

    for _ in tqdm(range(TOTAL_BATCH)):
        results = run_pipeline(batch_size=BATCH_SIZE)
        all_results.extend(results)

    file_path = save_results(all_results)

    print(f"完成，总生成内容数: {len(all_results)}")
    print(f"保存路径: {file_path}")

if __name__ == "__main__":
    main()
