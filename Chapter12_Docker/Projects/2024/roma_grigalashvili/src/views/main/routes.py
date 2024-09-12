from flask import render_template, Blueprint
from os import path
from src.models import Score, Quiz, User
from sqlalchemy.orm import joinedload
from src.config import Config

TEMPLATES_FOLDER = path.join(Config.BASE_DIRECTORY, "templates", "main")
main_blueprint = Blueprint("main", __name__, template_folder=TEMPLATES_FOLDER)

@main_blueprint.route("/")
def index():
    return render_template("index.html")

@main_blueprint.route("/highscores")
def highscores():
    # Fetch all scores
    scores = (
        Score.query
        .order_by(Score.quiz_id, Score.score.desc(), Score.time_taken)
        .all()
    )
    
    # Load quiz and user details
    quizzes = {quiz.id: quiz for quiz in Quiz.query.all()}
    users = {user.id: user for user in User.query.all()}

    # Process scores to get top 2 for each quiz
    quiz_scores = {}
    for score in scores:
        quiz_id = score.quiz_id
        if quiz_id not in quiz_scores:
            quiz_scores[quiz_id] = []
        quiz_scores[quiz_id].append(score)
    
    top_scores = []
    for quiz_id, scores_list in quiz_scores.items():
        # Sort scores by score and then by time_taken (ascending) if scores are equal
        sorted_scores = sorted(scores_list, key=lambda s: (-s.score, s.time_taken or float('inf')))
        top_two_scores = sorted_scores[:2]
        for score in top_two_scores:
            top_scores.append({
                "username": users[score.user_id].username,
                "email": users[score.user_id].email,
                "quiz_name": quizzes[score.quiz_id].quiz_name,
                "formatted_time": format_time(score.time_taken) if score.time_taken else "N/A",
                "score": score.score
            })

    return render_template("highscores.html", top_scores=top_scores)

def format_time(seconds):
    if seconds is None:
        return "N/A"
    minutes = int(seconds // 60)
    second = int(seconds % 60)
    return f"{minutes} minutes and {second} seconds"
