websites = {
    "israel": {
      "news": 'https://www.ynet.co.il/',
      "economy": 'https://www.themarker.com/',
      "sports": 'https://www.one.co.il/'
    },
    "usa": {
      "news": 'https://www.cnn.com/',
      "economy": 'https://www.wsj.com/',
      "sports": 'https://www.espn.com/'
    },
    "uk": {
      "news": ' https://www.bbc.com/news/',
      "economy": 'https://www.ft.com/',
      "sports": 'https://www.bbc.com/sport/'
    },
    "canada": {
      "news": 'https://www.cbc.ca/news/',
      "economy": 'https://www.theglobeandmail.com/',
      "sports": 'https://www.sportsnet.ca/'
    },
    "germany": {
      "news": ' https://www.ard.de/',
      "economy": 'https://www.handelsblatt.com/',
      "sports": 'https://www.kicker.de/'
    }
  }


# @app.route('/uk', methods=["GET"])
# def uk_websites():
#     """
#     Endpoint to get websites for UK.
#     ---
#     responses:
#       200:
#         description: A JSON object containing websites for UK.
#       404:
#         description: country Not Found
#     """
#     return jsonify(websites["uk"])
# @app.route('/canada', methods=["GET"])
# def canada_websites():
#     """
#     Endpoint to get websites for Canada.
#     ---
#     responses:
#       200:
#         description: A JSON object containing websites for Canada.
#       404:
#         description: country Not Found
#     """
#     return jsonify(websites["canada"])

# @app.route('/germany', methods=["GET"])
# def germany_websites():
#     """
#     Endpoint to get websites for Germany.
#     ---
#     responses:
#       200:
#         description: A JSON object containing websites for Germany.
#       404:
#         description: country Not Found
#     """
#     return jsonify(websites["germany"])

# @app.route('/israel', methods=["GET"])
# def israel_websites():
#     """
#     Endpoint to get websites for Israel.
#     ---
#     responses:
#       200:
#         description: A JSON object containing websites for Israel.
#       404:
#         description: country Not Found
#     """
#     return jsonify(websites["israel"])

# @app.route('/israel/news', methods=["GET"])
# def israel_news_websites():
#     """
#     Endpoint to get websites for Israel.
#     ---
#     responses:
#       200:
#         description: A JSON object containing websites for Israel.
#       404:
#         description: country Not Found
#     """
#     return jsonify(websites["israel"]['news'])