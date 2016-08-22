# FEC API wrapper

by Jake Kara
jkara@trendct.org

#### Example 1: Quickstart

     >>> from fec import Fec
     >>> conn = Fec(YOUR_API_KEY)
     >>> ret = conn.get("/candidates")
     >>> print ret

#### Example 2: Optionals

    ret = conn.get("/candidates",
                   pages=[1,2,3,4,5], # Specify which pages to retrieve
                   params="&cycle=2012&cycle=2016&office=P") #Specify parameters

#### Unstable code warning!

At the moment I don't have plans to develop this into a stable and
backwards compatible code base. I haven't added a lot of conveniences
likehard-coding queries you can make. I'm publishing this code in case
someone else finds it useful to see how to build a quick API wrapper.


Here are some features I do plan to add:

1. A parameter-forming method so you don't have to pass
all the URL parameters in one mashed-up string.

2. A method to get all pages of results

3. Rate limit-friendliness? Maybe I'll make this prevent you from
running over API rate limits. Maybe not.

4. Maybe I will add convenience methods for common queries.