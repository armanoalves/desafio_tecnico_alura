from app import db
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import ForeignKey

# Tabela do feedback do usuário
class Feedback(db.Model):
    __tablename__ = "feedbacks"

    id: Mapped[int] = mapped_column(primary_key=True)
    feedback: Mapped[str] = mapped_column(nullable=True)
    sentiments: Mapped[list["Sentiment"]] = relationship("Sentiment", back_populates="feedback")

    def __init__(self, feedback) -> None:
        self.feedback = feedback

# Tabela da análise de sentimentos
class Sentiment(db.Model):
    __tablename__ = "sentiments"
    
    id: Mapped[int] = mapped_column(primary_key=True)
    sentiment: Mapped[str] = mapped_column(nullable=True)
    feedback_id = mapped_column(ForeignKey("feedbacks.id"))
    requested_features: Mapped[list["Requested_features"]] = relationship("Requested_features", back_populates="sentiment")
    feedback: Mapped["Feedback"] = relationship("Feedback", back_populates="sentiments")

    def __init__(self, sentiment, feedback_id) -> None:
        self.sentiment = sentiment
        self.feedback_id = feedback_id

# Tabela de funcionalidades analisadas no feedback
class Requested_features(db.Model):
    __tablename__ = "requested_features"
    
    id: Mapped[int] = mapped_column(primary_key=True)
    code: Mapped[str] = mapped_column(nullable=False)
    reason: Mapped[str] = mapped_column(nullable=True)
    sentiment_id = mapped_column(ForeignKey("sentiments.id"))
    sentiment: Mapped["Sentiment"] = relationship("Sentiment", back_populates="requested_features")

    def __init__(self, code, reason, sentiment_id) -> None:
        self.code = code
        self.reason = reason
        self.sentiment_id = sentiment_id
