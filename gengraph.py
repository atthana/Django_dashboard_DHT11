# -*- coding: utf-8 -*-
def GenGraph(header = ['Jan','Feb','Mar'],temp = [20,33,50],title='Temp (c)'):
	data1 = """

	<!doctype html>
	<html>

	<head>
		<title>Temperature in LQID360</title>
		<script src="https://www.chartjs.org/dist/2.8.0/Chart.min.js"></script>
		<script src="https://www.chartjs.org/samples/latest/utils.js"></script>
		<style>
		canvas {
			-moz-user-select: none;
			-webkit-user-select: none;
			-ms-user-select: none;
		}
		</style>
	</head>

	<body>
		<div class="container">
		<div class="wrapper">
			<canvas id="Graph"></canvas>
		</div>
		</div>
		
		<script>


		var config = {
			type: 'line',
			data: {
				labels: ['"""


	data2 ="""'],
				datasets: [{
					label: '"""

	data20 = title

	data21="""',
					backgroundColor: window.chartColors.red,
					borderColor: window.chartColors.red,
					fill: false,
					data: [
					"""
	data2 = data2 + data20 + data21

	data3= '''],
				}]
			},
			options: {
				responsive: true,
				title: {
					display: true,
					text: 'Temperature Sensor DHT11'
				},
				scales: {
					xAxes: [{
						display: true,
					}],
					yAxes: [{
						display: true,
						
					}]
				}
			}
		};

		window.onload = function() {
			var ctx = document.getElementById('Graph').getContext('2d');
			window.myLine = new Chart(ctx, config);
		};

		</script>
	</body>

	</html>'''


	#header = ['Jan','Feb','Mar']
	#temp = [20,33,50]


	data_header = "','".join(str(x) for x in header)
	data_temp = ','.join(str(x) for x in temp)

	allhtml = '{}{}{}{}{}'.format(data1,data_header,data2,data_temp,data3)

	print(allhtml)

	with open('graph.html','w') as f:
		f.write(allhtml)

#GenGraph(['10:00','11:00','12:00','13:00','14:00','15:00','16:00'],[3,9,6,3,4,9,10])

#date = ['Mon','Tue','Wed','Thu','Fri']
#sales = [50,55,43,20,40]

#GenGraph(date,sales,'sales')
