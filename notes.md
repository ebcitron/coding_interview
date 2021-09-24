Im going to need to use python to parse through the json.

    research syntax and variable assignment.

    figure out how to link the user_id to the name of the person

    look up ways python handles dates/times
        and if the problem is providing times they are available or already booked.

create a script to ...
    search for and return the open schedules of x names inputed
        for multiple people, do I only return times they are ALL available? 
        or should I return each inputted names availability, one after another?
        --Must return free time that works for EVERY input employee


    take in names of who is being searched

    returns the times they are available


        refresh memory on working with dates/time in python(comparison, creating a "timesfree" from the inverse/negative of times they are booked)


    should I split each array up by day and the work hours?


    I think ill ....

    return each days availability


    so parse through and create a list of that employees appointments for the 5th, 6th, and 7th.

    merge overalapping intervals for multiple employee name inputs, find the remaining schedule free time and return per day

    start= 2021-07-05T13:00:00
    end = 2021-07-07T21:00:00



    ------------------------------------------------------------------------------------------------------------

    Ive done some research into python datetime library. Im thinking about how to manage the whole "Were scheduling things at 15 min intervals but be able to handle an 1136-1249 type situation".
                    Not sure how itl effect runtime, but im going to take it one day at a time... literally. Starting at 13 ending at 21, instead of working it as multiple days with those times being "booked". Or I could just display them seperate by day in the return fn if its quicker/less expensive.

                    
-------------------------------------------------------------------------------------------Day 2------------------------------
---------------------------------------------------------------
SO... ive got the functions written to return the appointments of anyone passed into the script. Today I need to...

    ultimately: Return the timeslots any combination of employees is available.

    to do this- I have to: figure out how to effectively return the timeslots that ARENT scheduled..
                so if Total hours T - scheduled S = desired result R                im looking for a way to choose the times in between those scheduled
                    regardless of how many overlapping schedules are fed into function..
                        so ill need a way to handle overlapping and sequential meetings, to treat them as one, longer meeting.

                        **Go study old notes on merge/sort stuff

                    Rather than processing the same time slots for each input, I should screen and clean up the data before putting it through the function ill write that results in our answer.

                    ##Personal note.. Re-learn the most efficient syntax currently hip in python 3.8.


                    Next ill want to figure out the most efficient way of handling the 9-5 schedule, and 3 individual days. 
                        The example has it seperated by day, so I could...

                        either add 21:00-13:00 into the equation as a list of default scheduled appointments, to be held back from result regardless of employee(s) searched for, and than display results by day...

                        OR... Handle a comparison of the time between 13:00-21:00, and each necessary appointment fed in, and do that per each day...

                        Currently looking into efficiency of each option...

                        For the final function, Ill have to compare the times

                    So im definately going to have to sort and merge the schedules, regardless of if I do it to the combined schedules of all inputed employees before feeding that in, or if I feed each employee into the function and than sort/merge the results for each inputted employee to return the combined availability.


                    I could translate the data into a format that can be easily compared regardless of the detail, minute, of the availability. So starting 21-07-05T13:00 as x=0, and translating every minute untill 21-07-07T21:00 as an x++ leading up to  43200
                        but may be unnecessary 


                    Ultimately im going to return the gaps between intervals of sorted/merged