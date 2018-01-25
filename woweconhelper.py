import sys
import time # Wibbly Wobbly
import praw # Python Reddit API Wrapper
# This WoWEconHelper bot was created by Hugh R. (/u/Nivarka) for Gumdrops and the woweconomy team. Permission to use, modify, reproduce or commercialise this script is given only to moderators of the woweconomy subreddit (https://www.reddit.com/r/woweconomy/)

#KEYWORD BANK. To update, simply add another string into 'single quotes'. To add another category, create a name for it as below, and add it into case selection.
prof = ['skill', 'prof', 'enchant', 'leather', 'tailor', 'alch', 'smith', 'engineer', 'inscription', 'jewelcrafting']
farm = ['farm', 'grind', 'gather', 'skin', 'collect', 'min', 'herb']
mission = ['mission', 'hall','champion']
new = ['new', 'noob', 'beginner', 'start', 'new', 'earn gold', 'make gold']
question = ['?', 'question']

response = 'Hey there {},\n\n \n\n Judging by the title of your post, it looks like you _*might*_ be asking a rather common question about {}. I think you might be able to find some useful information in the following places:\n\n{}\n\n{}\n\n If these resources help you out sufficiently, please could you consider deleting this post? If these are not helpful, just ignore me!\n\n \n\n *I am a bot! This reply was triggered based on the title of your post. Please contact the subreddit moderators if you have any feedback on me.*'
starttime = time.time()

def main():
        sys.stdout.write("\x1b]2;WoWEconHelper\x07")
        reddit = praw.Reddit('woweconhelper')
        subreddit = reddit.subreddit('woweconomy')
        print('{}: Bot loaded!'.format(time.strftime("%d-%m-%y %H:%M")))
        for submission in subreddit.stream.submissions():
                answer_questions(submission)


def answer_questions(submission):

        
        caught = 0
        lower_title = submission.title.lower()

        if submission.created_utc > starttime:
                print('{}: Scanning: {}'.format(time.strftime("%d-%m-%y %H:%M"), submission.title.encode('ascii', 'ignore')))
                for kw in prof:
                        if kw in lower_title:
                                for q in question:
                                        if q in lower_title and caught == 0:
                                                topic = 'professions'
                                                print('{}: Responding...'.format(time.strftime("%d-%m-%y %H:%M")))
                                                submission.reply(response.format(submission.author, topic, "https://www.reddit.com/r/woweconomy/comments/6js3ka/how_do_i_make_gold_and_co/", "https://www.reddit.com/r/woweconomy/comments/6oizli/the_lazy_goldmakers_total_legion_gold_guide/"))
                                                caught = 1
                                                break
                        
                for kw in farm:
                        if kw in lower_title:
                                for q in question:
                                        if q in lower_title and caught == 0:
                                                topic = 'farming'
                                                print('{}: Responding...'.format(time.strftime("%d-%m-%y %H:%M")))
                                                submission.reply(response.format(submission.author, topic, "https://www.reddit.com/r/woweconomy/comments/6oizli/the_lazy_goldmakers_total_legion_gold_guide/", "https://www.reddit.com/r/woweconomy/wiki/raidgrinding"))
                                                caught = 1
                                                break

                for kw in mission:
                        if kw in lower_title:
                                for q in question:
                                        if q in lower_title and caught == 0:
                                                topic = 'missions or orderhalls'
                                                print('{}: Responding...'.format(time.strftime("%d-%m-%y %H:%M")))
                                                submission.reply(response.format(submission.author, topic, "https://www.reddit.com/r/woweconomy/comments/7oloe0/my_order_hall_spreadsheet/", "https://www.reddit.com/r/woweconomy/comments/77i7wv/73_order_hall_mission_guide/"))
                                                caught = 1
                                                break
                                        
                for kw in new:
                        if kw in lower_title and caught == 0:
                                        topic = 'getting started with gold making'
                                        print('{}: Responding...'.format(time.strftime("%d-%m-%y %H:%M")))
                                        submission.reply(response.format(submission.author, topic, "https://www.reddit.com/r/woweconomy/comments/7nbe98/a_gift_to_close_out_2017_the_definitive_newbie/", "https://www.reddit.com/r/woweconomy/comments/6oizli/the_lazy_goldmakers_total_legion_gold_guide/"))
                                        caught = 1
                                        break

                print('{}: Completed: {}'.format(time.strftime("%d-%m-%y %H:%M"), submission.title))
		


if __name__ == '__main__':
    main()
