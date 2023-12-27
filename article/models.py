from django.db import models
from django.db.models import TextChoices


# Create your models here.
class Article(models.Model):
    class Category(TextChoices):
        QNA = "QNA", "질문과 답변"
        NOTICE = "NOTICE", "공지사항"
        FREE = "FREE", "자유게시판"

    objects = models.Manager
    author: int = models.IntegerField
    title: str = models.CharField(
        max_length=255, db_column="title", help_text="제목을 입력해주세요.",
        db_comment="게시글 제목입니다."
    )
    content: str = models.TextField(
        db_column="content", help_text="내용을 입력해주세요.",
        db_comment="게시글 내용입니다."
    )
    category: str = models.CharField(
        max_length=255, db_column="category", choices=Category.choices,
        help_text="카테고리를 선택해주세요.", db_comment="게시글 카테고리입니다."
    )
    view_count: int = models.IntegerField(
        db_column="view_count", default=0, help_text="조회수입니다.",
        db_comment="게시글 조회수입니다."
    )
    created_date: str = models.DateTimeField(
        auto_now_add=True, db_column="created_date", help_text="생성일을 입력해주세요."
    )
    last_modified_date: str = models.DateTimeField(
        auto_now=True, db_column="last_modified_date", help_text="수정일을 입력해주세요."
    )

    class Meta:
        db_table = "article"
        db_table_comment = "게시글"
        get_latest_by = ("last_modified_date", "created_date")
        ordering = ("last_modified_date", "created_date")
        constraints = [
            models.UniqueConstraint(
                fields=["title", "author"], name="unique_title_author"
            )
        ]
