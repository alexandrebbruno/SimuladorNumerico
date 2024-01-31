function plotHeatmapCFD(result){
    // Plot the simulation results in a heatmap
    var colorscaleValue = [
        [0, '#0b7eff'],
        [1, '#f10300']
    ];

    var data = [
        {
            x: result.x,
            y: result.y,
            z: result.z,
            type: 'heatmap',
            colorscale: colorscaleValue,
            showscale: false
        }
    ];
    Plotly.newPlot('heatmap_id', data, {
        title: 'Temperature',
        width: 800,
        height: 600
    });
}

function plotGeochemicalData(result){
    // Plot the simulation results in a heatmap
    var data = [
        {
            x: result.temperatures,
            y: result.densities,
            showscale: false
        }
    ];
    Plotly.newPlot('density_id', data, {
        title: 'Densities',
        width: 800,
        height: 600
    });
}

function getCFDData(){
    // get any input values from the form
    var form_data = {
        // replace these with the names of your input fields
        'Nx': $('#Nx').val(),
        'Ny': $('#Ny').val(),
        'Lx': $('#Lx').val(),
        'Ly': $('#Ly').val(),
        'Tw': $('#Tw').val(),
        'Te': $('#Te').val(),
        'Tn': $('#Tn').val(),
        'Ts': $('#Ts').val(),
        'total_t': $('#total_t').val(),
        'ro': $('#ro').val(),
        'k': $('#k').val(),
        'cp': $('#cp').val(),
    };

    return form_data;
}

function getGeochemicalData(){
    // get any input values from the form
    var form_data = {
        // replace these with the names of your input fields
        'temp_min': $('#temp_min').val(),
        'temp_max': $('#temp_max').val(),
        'pressure': $('#pressure').val(),
        'cl': $('#cl').val(),
        'na': $('#na').val(),
        'so4': $('#so4').val(),
        'mg': $('#mg').val(),
        'ca': $('#ca').val(),
        'k': $('#k').val(),
        'hco3': $('#hco3').val(),
        'br': $('#br').val(),
        'co3': $('#co3').val(),
        'sr': $('#sr').val(),
    };

    return form_data;
}

function simulateCFD() {
    // Make an AJAX request to the Flask endpoint to start the simulation
    $.ajax({
        type: 'POST',
        url: '/CFDSimulationProxy',
        data: JSON.stringify(getCFDData()),
        contentType: 'application/json;charset=UTF-8',
        success: function(result) {
            plotHeatmapCFD(result);
        },
        error: function(xhr, status, error) {
            alert('Error: ' + error);
        }
    });
}

function simulateGeo() {
    // Make an AJAX request to the Flask endpoint to start the simulation
    $.ajax({
        type: 'POST',
        url: '/GeochemicalSimulationProxy',
        data: JSON.stringify(getGeochemicalData()),
        contentType: 'application/json;charset=UTF-8',
        success: function(result) {
            plotGeochemicalData(result);
        },
        error: function(xhr, status, error) {
            alert('Error: ' + error);
        }
    });
}

$(document).ready(function() {
    // Attach a click event listener to the "Simulate" button
    $('#simulate-btn-cfd').click(function() {
        simulateCFD();
    });
});

$(document).ready(function() {
    // Attach a click event listener to the "Simulate" button
    $('#simulate-btn-geo').click(function() {
        simulateGeo();
    });
});