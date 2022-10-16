let modal=document.querySelector('._aano')
let scrollHeight=modal.scrollHeight
let current=0
let interval=setInterval(()=>{
    modal.scroll(0,current)
    current+=100
    if (current>=scrollHeight){
        clearInterval(interval)
    }
})
