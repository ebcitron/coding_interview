Im going to need to use python to parse through the json.

    research syntax and variable assignment.

    figure out how to link the user_id to the name of the person

    look up ways python handles dates/times
        and if the problem is providing times they are available or already booked.

create a script to ...
    search for and return the open schedules of x names inputed
        for multiple people, do I only return times they are ALL available? 
        or should I return each inputted names availability, one after another?
        
        Must return free time that works for EVERY input employee


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

                    