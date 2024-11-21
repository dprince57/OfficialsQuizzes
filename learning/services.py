def award_badge(user_progress, badge_name):
    if badge_name not in user_progress.badges:
        user_progress.badges.append(badge_name)
        user_progress.save()
