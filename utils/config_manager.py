import os

facebook_user = os.getenv('FACEBOOK_USER', 'gustavo.leivas.142')
twitter_user = os.getenv('TWITTER_USER', 'GustavoLeivas2')
env_webdriver = os.getenv('WEBDRIVER', 'firefoxheadless')

config_list = {
    'facebook_origin': 'https://facebook.com/{user}'.format(user=facebook_user),
    'twitter_origin': 'https://twitter.com/{user}'.format(user=twitter_user),
}
