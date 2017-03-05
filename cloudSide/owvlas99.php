<?php
// retrieve the current weather in Amsterdam in degrees Celcius
$json = file_get_contents('http://api.openweathermap.org/data/2.5/forecast?q=SanPedroSula,HN&units=metric&appid=709ad769a8432a1a909fa58a22d86b91');
// parse the JSON
$data = json_decode($json);

// show the city (and the country)
//echo '<h1>', $data->city->name, ' (', $data->city->country, ')</h1>';

//create master array
$masterArray = array();
for ($x = 0; $x <= 39; $x++) {
	$dataArray = array("timestamp" => $data->list[$x]->dt_txt,
                		"temp_min" => $data->list[$x]->main->temp_min,
                		"temp_max" => $data->list[$x]->main->temp_max,
                		"pressure" =>  $data->list[$x]->main->pressure,
                		"humidity" => $data->list[$x]->main->humidity,
                		"weather" => $data->list[$x]->weather[0]->description);
	//echo '<pre>'; print_r($dataArray); echo '</pre>';


    array_push($masterArray, $dataArray);
} //end for loop
echo '<pre>'; print_r($masterArray); echo '</pre>';
?>
