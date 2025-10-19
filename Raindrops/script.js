var c = document.getElementById("myCanvas");
var ctx = c.getContext("2d");

raindrops = [];

var wind = 0;

function getRandom(min, max) {
    return Math.random() * (max - min) + min;
}

function gameLoop() {
    // Set color to white
    ctx.fillStyle = "white";

    // Draw a white rectangle over entire canvas
    // This will clear the canvas for next frame
    ctx.rect(0, 0, c.width, c.height);

    // Set color to white
    ctx.fill();

    // Create a new raindrop object
    // x = random from 0 to the width of the canvas
    // y = 0, at the top of the canvas
    // yspeed = random from 3 to 6 
    var raindrop = {
        x: getRandom(-2000, c.width+2000),
        y: 0,
        yspeed: Math.random() * 3 + 3,
    }

    // Append raindrop
    raindrops.push(raindrop);

    // Getting number of raindrop
    var k = raindrops.length

    // Iterates raindrop in reverse order
    /**
    
    If you do forward, there's a problem
    ---------
    You're removing an item, so the array gets shorter and the indexes shift — which can cause the loop to skip the next item.
    
    Suppose raindrops = [drop0, drop1, drop2]
    You remove drop1 at k = 1.
    Now the array becomes [drop0, drop2], but k moves on to 2, skipping over drop2.
    
    */
    while (k--) {

        // Gets the raindrop from the last one
        var drop = raindrops[k];

        // Move raindrop downward
        drop.y = drop.y + drop.yspeed;

        // Move raindrop left and right based on wind
        drop.x = drop.x + wind;

        // If raindrop has fallen below canvas, remove
        if (drop.y > c.height) {

            // Splice - add or remove
            // k = index/position
            // 1 = how many items will get removed
            // We can add next parameter which will be the new item to be inserted on index k
            raindrops.splice(k, 1);
            console.log(k)
        }

        // Otherwise, raindrop will be a blue rectangle
        else {
            ctx.beginPath()
            ctx.rect(drop.x, drop.y, 2, 4);
            ctx.fillStyle = "blue";
            ctx.fill();
        }
    }
}

// Animation
setInterval(gameLoop, 30);

document.addEventListener("keydown", keyDownHandler, false);

function keyDownHandler(e) {
    if (e.keyCode == 37) { //left
        wind--;
    } else if (e.keyCode == 39) { // right
        wind++;
    }
}