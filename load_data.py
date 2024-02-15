import os
from fastapi import BackgroundTasks
from app.core.config import settings
from app.db.session import SessionLocal
from app.models import Category, Region, Video
from scripts.parsers import parse_category_data, parse_video_data, parse_json_file
import pandas as pd


def load_data_task():
    print("Started Loading Data")
    with SessionLocal() as db:
        data_folder = settings.DATA_FOLDER

        for file_name in os.listdir(data_folder):
            if file_name.endswith("_category_id.json"):
                region_code = file_name.split("_")[0]
                print(f"Started loading region: {region_code}")

                category_data_path = os.path.join(data_folder, file_name)
                category_data = parse_json_file(category_data_path)

                parse_category_data(db, category_data, region_code)

                videos_data_path = os.path.join(data_folder,f"{region_code}videos.csv")
                video_data = pd.read_csv(videos_data_path, encoding='latin-1')
                parse_video_data(db, video_data, region_code)

                


if __name__ == '__main__':
    load_data_task()