var queue_implementation = function(input){
	var instructions = input.split('\n');
	var num_queries = parseInt(instructions[0]);

	var queue = new Array();
	var query = '';
	var head = 0;

	for(let i = 1; i <= num_queries; i++){
		query = instructions[i];
		if(query.length > 1){
			query = query.split(' ');
			queue.push(parseInt(query[1]));
		}
		else if(query === '2'){
			queue.shift();
		}
		else {
			console.log(queue[head]);
		}
	}

	//console.log(queue);
}

queue_implementation('10\n1 42\n2\n1 14\n3\n1 28\n3\n1 60\n1 78\n2\n2');