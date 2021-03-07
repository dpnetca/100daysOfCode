#!/usr/bin/env python
from ig_follower import InstaFollower

ig_follower = InstaFollower()

ig_follower.login()
ig_follower.find_followers()
ig_follower.follow()

ig_follower.quit()
