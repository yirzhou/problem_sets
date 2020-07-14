class Solution:
    def angleClock(self, hour: int, minutes: int) -> float:
        """#1344. Given two numbers, hour and minutes. 
        Return the smaller angle (in degrees) formed between the hour and the minute hand.
        """
        hour = hour%12
        hour_min = (hour+minutes/60)*5
        angle = abs(hour_min-minutes)*6
        return angle if angle < 180 else (360-angle)
    