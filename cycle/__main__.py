import constants
# from cycle.constants import GREEN
from constants import GREEN
from constants import RED

from game.casting.cast import Cast
from game.casting.growth import Growth
from game.casting.score import Score
from game.casting.cycle import Cycle
from game.scripting.script import Script
from game.scripting.control_actors_action import ControlActorsAction
from game.scripting.move_actors_action import MoveActorsAction
from game.scripting.handle_collisions_action import HandleCollisionsAction
from game.scripting.draw_actors_action import DrawActorsAction
from game.directing.director import Director
from game.services.keyboard_service import KeyboardService
from game.services.video_service import VideoService
from game.shared.color import Color
from game.shared.point import Point


def main():
    
    # create the cast
    cast = Cast()
    cast.add_actor("growths", Growth())
    # cast.add_actor("snakes", Snake())
    cast.add_actor("cycles", Cycle(constants.RED))
    cast.add_actor("cycles", Cycle(constants.GREEN))
    cast.add_actor("scores", Score())
   
    # start the game
    keyboard_service = KeyboardService()
    video_service = VideoService()

    script = Script()
    script.add_action("input", ControlActorsAction(keyboard_service))
    script.add_action("update", MoveActorsAction())
    script.add_action("update", HandleCollisionsAction())
    script.add_action("output", DrawActorsAction(video_service))
    script.add_action("update", Growth())
    
    director = Director(video_service)
    director.start_game(cast, script)


if __name__ == "__main__":
    main()