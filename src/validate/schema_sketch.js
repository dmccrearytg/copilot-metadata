
function setup() {
    createCanvas(800, 600);
    noLoop();
}

function draw() {
    background(255);
    drawSchema();
}

function drawSchema() {
    const fields = {
        "ApplicationID": {
            "type": "string", "_comment": "Unique identifier for the application."
        },
        "ApplicationName": {
            "type": "string", "_comment": "Human-readable name of the application.  It should be short and not include classifiers such as 'knowledge graph'."
        },
        "ApplicationDescription": {
            "type": "string", "_comment": "Detailed description of what the application does.  Focus on how the application is used to solve business problems"
        },
        "Owner": {
            "type": "string", "_comment": "Name of the owner or responsible party for the application."
        },
        "TargetAvailabilityDate": {
            "type": "string", "_comment": "The timeframe we would like this application to be available to our customers.  This is currently a freeform text."
        },
        "GraphAlgorithms": {
            "type": "string", "_comment": "A list of the graph algorithms used in this solution kit separated by commas."
        },
        "GraphFeatures": {
            "type": "string", "_comment": "A list of the graph algorithms used in this solution kit separated by commas."
        },
        "ROIDashboardMetrics": {
            "type": "string", "_comment": "A list of the graph algorithms used in this solution kit separated by commas."
        },
        "MLModels": {
            "type": "string", "_comment": "A list of the machine-learning models used in this solution kit separated by commas"
        },
        "CurrentDevelopmentStatus": {
            "type": "string", "enum":[ "not-started", "in-development", "done"], "_comment": "Current stage in the development lifecycle of the application."
        },
        "Personas": {
            "type": "array", "items": {
                "type": "string"
            },
            "minItems": 0, "_comment": "Optional. List of personas representing typical users of the application."
        },
        "Questions": {
            "type": "array", "items": {
                "type": "object", "properties": {
                    "QuestionID": {
                        "type": "string"
                    },
                    "QuestionText": {
                        "type": "string"
                    },
                    "QuestionPriority": {
                        "type": "string", "enum":[ "critical", "high", "medium", "low"]
                    },
                    "QuestionParameters": {
                        "type": "array", "items": {
                            "type": "object", "properties": {
                                "ParameterName": {
                                    "type": "string"
                                },
                                "ParameterValue": {
                                    "type": "string"
                                }
                            },
                            "required":[ "ParameterName", "ParameterValue"]
                        }
                    },
                    "GSQL_Query": {
                        "type": "string"
                    },
                    "GSQL_QueryStatus": {
                        "type": "string", "enum":[ "not-started", "in-development", "done"]
                    }
                },
                "required":[ "QuestionID", "QuestionText", "QuestionPriority", "GSQL_Query", "GSQL_QueryStatus"], "_comment": "Details about the questions to be addressed by the chatbot application."
            }
        }
    };
    const requiredFields = new Set ([ "ApplicationID", "ApplicationName", "ApplicationDescription", "Owner", "CurrentDevelopmentStatus", "Questions"]);
    let yPos = 20;
    
    for (let key in fields) {
        const isRequired = requiredFields.has(key);
        const comment = fields[key][ '_comment'];
        drawField(key, yPos, isRequired, comment);
        yPos += 60;
    }
}

function drawField(key, yPos, isRequired, comment) {
    fill(220);
    strokeWeight(2);
    stroke(isRequired ? 0: 100);
    if (! isRequired) {
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