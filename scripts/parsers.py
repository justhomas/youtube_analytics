import json
import pandas as pd
from sqlalchemy.orm import Session
from app.models import Category, Video, Region

def parse_json_file(file_path):
    with open(file_path, "r", encoding="utf-8") as file:
        data = json.load(file)
    return data

def parse_video_data(db: Session, video_data, region_code):
    # Implement video data parsing logic using Pandas DataFrame
    df = pd.DataFrame(video_data)

    # Identify region based on region_code and insert into the Region table if not exists
    region = db.query(Region).filter_by(code=region_code).first()

    # Insert videos into the Video table
    for _, row in df.iterrows():
        category_id = row["category_id"]
        category = db.query(Category).filter_by(category_id=category_id).first()
        
        video = Video(
            video_id=row["video_id"],
            trending_date=row["trending_date"],
            title=row["title"],
            channel_title=row["channel_title"],
            category=category,
            publish_time=row["publish_time"],
            tags=row["tags"],
            views=row["views"],
            likes=row["likes"],
            dislikes=row["dislikes"],
            comment_count=row["comment_count"],
            thumbnail_link=row["thumbnail_link"],
            comments_disabled=row["comments_disabled"],
            ratings_disabled=row["ratings_disabled"],
            video_error_or_removed=row["video_error_or_removed"],
            description=row["description"],
            region=region
        )
        db.add(video)

    db.commit()

def parse_category_data(db: Session, category_data, region_code):
    # Implement category data parsing logic
    region = db.query(Region).filter_by(code=region_code).first()
    if not region:
        region = Region(code=region_code)
        db.add(region)
        db.commit()

    for item in category_data["items"]:
        category = db.query(Category).filter_by(category_id=item["id"]).first()
        if not category:
            category = Category(
                title=item["snippet"]["title"],
                category_id = item["id"]
            )
            db.add(category)

        # Add the relationship between the region and category
        if region not in category.regions:
            category.regions.append(region)

    db.commit()
