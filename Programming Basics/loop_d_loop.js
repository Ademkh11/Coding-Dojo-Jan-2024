/* 1) How do we know we need a loop here?
 we khnow that we need a loop here because we have from were we can start the loop , where it should stop and the steps we should take 
2) What's the starting point of the loop?
the loop starts from 0  
3) When should the loop stop?
 the loop should stop when it reaches 6 miles 
4) How will the loop know when to stop?
the loop will know when to stop only if you put a limit to it by using a certain condition 
5) What's incrementing for each iteration of the loop?
what is incrementing for each iteration of the loop is the distance by miles achieved by the runner. It increments by 2 
6) What variables do we need?
we need only one variable related to the distance runned by the runner 
*/
var i = [0,1,2,3,4,5,6]
for(var i = 0; i < 6; i+2){
    if (i < 6){
        console.log("pops out a piece of candy")
    } 
    else{
    console.log("stop giving candy out")
    } 
}