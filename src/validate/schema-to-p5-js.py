import json

# Load the JSON Schema
with open('schema.json', 'r') as file:
    schema = json.load(file)

# Prepare the p5.js sketch setup
p5js_code = """
function setup() {
    createCanvas(800, 600);
    noLoop();
}

function draw() {
    background(255);
    drawSchema();
}

function drawSchema() {
    const fields = """ + json.dumps(schema['properties']) + """;
    const requiredFields = new Set(""" + json.dumps(schema['required']) + """);
    let yPos = 20;

    for (let key in fields) {
        const isRequired = requiredFields.has(key);
        const comment = fields[key]['_comment'];
        drawField(key, yPos, isRequired, comment);
        yPos += 60;
    }
}

function drawField(key, yPos, isRequired, comment) {
    fill(220);
    strokeWeight(2);
    stroke(isRequired ? 0 : 100);
    if (!isRequired) {
        drawingContext.setLineDash([5, 15]);
    } else {
        drawingContext.setLineDash([]);
    }
    rect(20, yPos, 760, 50);
    fill(0);
    noStroke();
    text(key + ': ' + comment, 30, yPos + 30);
}

function mouseMoved() {
    redraw();
}
"""

# Save the p5.js sketch to a new file
with open('schema_sketch.js', 'w') as file:
    file.write(p5js_code)
