let chart;

fetch("/clusters")

.then(res => res.json())

.then(data => {

let cluster0 = []
let cluster1 = []
let cluster2 = []
let cluster3 = []
let cluster4 = []

data.forEach(p => {

if(p.cluster == 0) cluster0.push({x:p.x,y:p.y})
if(p.cluster == 1) cluster1.push({x:p.x,y:p.y})
if(p.cluster == 2) cluster2.push({x:p.x,y:p.y})
if(p.cluster == 3) cluster3.push({x:p.x,y:p.y})
if(p.cluster == 4) cluster4.push({x:p.x,y:p.y})

})

const ctx = document.getElementById("clusterChart")

chart = new Chart(ctx, {

type: "scatter",

data: {

datasets: [

{label:"Cluster 0",data:cluster0,backgroundColor:"red"},
{label:"Cluster 1",data:cluster1,backgroundColor:"blue"},
{label:"Cluster 2",data:cluster2,backgroundColor:"green"},
{label:"Cluster 3",data:cluster3,backgroundColor:"purple"},
{label:"Cluster 4",data:cluster4,backgroundColor:"orange"}

]

},

options:{

animation:{
duration:1500
},

plugins:{
legend:{
position:"top"
},
tooltip:{
enabled:true
}
},

scales:{
x:{
title:{
display:true,
text:"Annual Income (k$)"
},
grid:{
color:"#e5e5e5"    
}
},

y:{
title:{
display:true,
text:"Spending Score (1-100)"
},
grid:{
color:"#e5e5e5"    
}
}
}
}

})

})



function predict(){

if(!chart){
alert("Chart still loading, please wait")
return
}    

let income = document.getElementById("income").value
let score = document.getElementById("score").value

fetch("/predict",{

method:"POST",

headers:{
"Content-Type":"application/json"
},

body:JSON.stringify({
income:income,
score:score
})

})

.then(res=>res.json())

.then(data=>{

let cluster = data.cluster

document.getElementById("result").innerHTML =
"Customer belongs to cluster : "+cluster

// highlight predicted point

chart.data.datasets.push({

label:"Prediction",
data:[{x:Number(income),y:Number(score)}],
backgroundColor:"yellow",
borderColor:"black",
borderWidth:2,
pointRadius:12

})

chart.update()

})

}