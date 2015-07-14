import random
from Brisk import Brisk
import time
import argparse

TEAM_NAME = 'Tasty Canned Meat'
_TOKEN = ''

class BriskPlayer():
    def await_turn_and_get_status(self, game):
        """" Waits for turn and gets status"""
        while True:
            status = game.get_player_status()
            if status['current_turn'] or status['eliminated'] or status['winner']:
                return status
            time.sleep(0.25)


    def run(self, game_num=None):

        game = Brisk(game_num, TEAM_NAME)
        print "starting game {} we are player {}".format(game.game_id, game.player_id)

        while True:
            status = self.await_turn_and_get_status(game)
            if status['eliminated']:
                print "we lost :-("
                break
            if status['winner']:
                if status['winner'] == game.player_id:
                    print "we won :-)"
                    res = game.reward()
                    print "send attachments to {}".format(res['upload_email'])
                else:
                    print "We lost without getting eliminated. Guess we timed out"
                break
            print "We survived to {} turns!".format(status['turns_taken'])
            lucky_territory = random.randint(0, len(status['territories']) - 1)
            game.place_armies(status['territories'][lucky_territory]['territory'], status['num_reserves'])
            game.end_turn()


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('-g', default=None, type=int, help="Optional. The game id to join, 0 if we're first")
    res = parser.parse_args()
    player = BriskPlayer()
    player.run(res.g)

if __name__ == '__main__':
    main()