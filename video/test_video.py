import unittest

from video.video import Video

class MyTestCase(unittest.TestCase):
    def setUp(self):
        self.video = Video("Flash", 60)

    def test_that_play_displays_that_the_vide_is_playing_now(self):

        self.assertEqual("Flash is now playing", self.video.play())  # add assertion here

    def test_that_the_playback_moves_forward_according_to_the_minutes_that_was_input(self):

        self.assertEqual(30, self.video.advance(30))

    def test_that_the_playback_moves_forward_according_to_the_minutes_that_was_input_and_once_the_minutes_pass_the_duration_of_the_video_it_throws_illegal_error(self):

        self.assertRaises(ValueError, self.video.advance, 80)

    def test_that_when_an_invalid_input_is_entered_as_the_minutes_it_throws_illegal_exception(self):

        self.assertRaises(ValueError, self.video.advance, -70)

    def test_that_it_returns_true_when_the_video_has_reached_the_end(self):

        self.video.advance(60)
        self.assertTrue(self.video.is_finished())

    def test_that_it_returns_false_when_the_video_has_not_reached_the_end(self):

        self.video.advance(20)
        self.assertFalse(self.video.is_finished())

    def test_that_when_the_video_is_advance_with_some_minutes_when_i_restart_it_resets_the_playback_back_to_the_beginning(self):

        self.assertEqual(30, self.video.advance(30))
        self.assertEqual(0, self.video.restart())

    def test_that_when_the_video_is_advance_with_some_minutes_and_I_check_how_many_minutes_are_left_before_the_video_ends_it_gives_me_the_subtracted_minutes(self):

        self.assertEqual(45, self.video.advance(45))
        self.assertEqual(15, self.video.time_remaining())


if __name__ == '__main__':
    unittest.main()
