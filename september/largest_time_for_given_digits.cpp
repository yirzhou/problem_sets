#include <iostream>
#include <string>
#include <vector>
/**
 * @brief Given an array arr of 4 digits, find the latest 24-hour time that can be made using each digit exactly once.
 * 24-hour times are formatted as "HH:MM", where HH is between 00 and 23, and MM is between 00 and 59. The earliest 24-hour time is 00:00, and the latest is 23:59.
 * Return the latest 24-hour time in "HH:MM" format.  If no valid time can be made, return an empty string.
*/
class Solution {
public:
    std::string largestTimeFromDigits(std::vector<int>& arr) {
        int largestTime = -1;

        for (int i = 0; i < 4; ++i) {
            for (int j = 0; j < 4; ++j) {
                if (j != i) {
                    for (int k = 0; k < 4; ++k) {
                        if (k !=i && k != j) {
                            int l = 6-i-j-k;

                            int result = helper(arr[i], arr[j], arr[k], arr[l]);

                            largestTime = std::max(result, largestTime);
                        }
                    }
                }
            }
        }

        if (largestTime == -1) 
            return "";
        
        int hours = largestTime/60, minutes = largestTime%60;
        std::string hourString = (hours == 0) ? "00" : std::to_string(hours);
        std::string minString = (minutes == 0) ? "00" : std::to_string(minutes);

        if (hourString.length() == 1) hourString = "0"+hourString;
        if (minString.length() == 1) minString = "0"+minString;
        return hourString + ":" + minString;
    }

    int helper(int a, int b, int c, int d) {
        int hours = a*10+b, min = c*10+d;

        if (hours < 24 && min < 60) {
            return hours * 60 + min;
        }
        return -1;
    }
};
