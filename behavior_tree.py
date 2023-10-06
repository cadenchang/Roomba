import bt_library as btl
from until_fails import UntilFails
from clean_floor import CleanFloor
from dusty_spot_check import DustySpotCheck
from done_general import DoneGeneral
from spot_cleaning_check import SpotCheck
from general_cleaning_check import GeneralCheck
from battery_less_than_30 import BatteryLessThan30
from find_home import FindHome
from go_home import GoHome
from succeed_task import SucceedTask
from globals import BATTERY_LEVEL, GENERAL_CLEANING, SPOT_CLEANING, DUSTY_SPOT_SENSOR, HOME_PATH
from sequence import Sequence
from priority import Priority
from done_spot import DoneSpot


low_battery = BatteryLessThan30()
find_home = FindHome()
go_home = GoHome()
dock = SucceedTask()

spot = SpotCheck()
clean_spot1 = SucceedTask()
clean_spot_timer = btl.Timer(20, clean_spot1)
done_spot = DoneSpot()
spot_sequence = Sequence([spot, clean_spot_timer, done_spot])

clean_spot2 = SucceedTask()
dusty_spot_timer = btl.Timer(35, clean_spot2)
dusty_spot_check = DustySpotCheck()
dusty_spot_sequence = Sequence([dusty_spot_check, dusty_spot_timer])

clean_floor = CleanFloor()
clean_floor_until = UntilFails(clean_floor)

general_check = GeneralCheck()
general_priority = Priority([dusty_spot_sequence, clean_floor_until])
done_general = DoneGeneral()
actively_cleaning_sequence = Sequence([general_priority, done_general])
general_cleaning_sequence = Sequence([general_check, actively_cleaning_sequence])

low_battery_sequence = Sequence([low_battery, find_home, go_home, dock])
command_selection = btl.Selection([spot_sequence, general_cleaning_sequence])
do_nothing = SucceedTask()


tree_root = Priority([low_battery_sequence, command_selection, do_nothing])