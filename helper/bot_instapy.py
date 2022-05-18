from instapy import InstaPy

# login
session = InstaPy(username='test', password='test', headless_browser=True, want_check_browser=False).login() #headless browser
# session = InstaPy(username="paralize.bot", password="randombot123_", want_check_browser=False).login()
# session.login()

# # like
# session.like_by_tags(["bmw", "mercedes"], amount=5)
# session.set_dont_like(["naked", "nsfw"]) #dont like

# # follow
# session.set_do_follow(True, percentage=50)

# # comment
# session.set_do_comment(True, percentage=50)
# session.set_comments(["Nice!", "Sweet!", "Beautiful :heart_eyes:"])

# # quota
# session.set_quota_supervisor(enabled=True, peak_comments_daily=240, peak_comments_hourly=21)

# # bound relation
# session.set_relationship_bounds(enabled=True, max_followers=8500)

session.end()