var balanced_brackets = function(str){
	var length = str.length;

	if(length < 2 || length%2 !== 0){
		console.log('NO');
	}
	else {

		var open_brackets = new Array();
		var brackets_map = {'[':']', '(':')', '{':'}'};
		var open_brackets_set = {'[':1,'{':1,'(':1};
		var last_open = '';
		var expected_bracket = '';
		var is_balanced = true;

		for(let i = 0; i < length; i++){
			if(open_brackets_set.hasOwnProperty(str[i])){
				open_brackets.push(str[i]);
			}
			else {
				last_open = open_brackets.pop();
				expected_bracket = brackets_map[last_open];

				if(expected_bracket !== str[i]){
					is_balanced = false;
					break;
				}
			}
		}

		(is_balanced && open_brackets.length === 0) ? console.log('YES') : console.log('NO');
	}
}

balanced_brackets('');