// ################################# Import modules
const fs = require("fs");
const readline = require("readline");
const mysql = require("mysql");
const async = require("async");
const axios = require("axios");
const request = require('request');
const utf8 = require('utf8');
const spawn = require("child_process").spawn;
const { exit } = require("process");
var config = require("./config.js");
const host = config.host;
const user = config.user;
const password = config.password;
const database = config.database;
const proxies = config.proxies;
const u_jsonip = config.u_jsonip;
const u_tweet = config.u_tweet;

// #################################Database Connection
var conn = mysql.createPool({
  host: host,
  user: user,
  password: password,
  database: database
});

// ################################# Define basic functions
if(typeof(String.prototype.trim) === "undefined")
{
    String.prototype.trim = function() 
    {
        return String(this).replace(/^\s+|\s+$/g, '');
    };
}

function shuffle(a) {
    for (let i = a.length - 1; i > 0; i--) {
        const j = Math.floor(Math.random() * (i + 1));
        [a[i], a[j]] = [a[j], a[i]];
    }
    return a;
}

function sleep(ms) {
    return new Promise(resolve => setTimeout(resolve, ms));
}

function randomInteger(min, max) {
  return Math.floor(Math.random() * (max - min + 1)) + min;
}

function r_word(words) {
	return words[randomInteger(0, words.length - 1)];
}

// #################################Define Custom functions
function make_random_sentence() {
	// let nouns = ["nouns1", "nouns2", "nouns3", "nouns4"];
	// let verbs = ["verbs1", "verbs2", "verbs3", "verbs4"];
	// let adv = ["adv1", "adv2", "adv3", "adv4"];
	// let adj = ["adj1", "adj2", "adj3", "adj4"];

	let nouns = ["the", "of", "to", "and"];
	let verbs = ["thing", "see", "him", "two"];
	let adv = ["big", "high", "such", "follow"];
	let adj = ["run", "don't", "while", "press"];

	let no_space_comment = [r_word(nouns), r_word(verbs), r_word(adv), r_word(adj), r_word(nouns), r_word(verbs), r_word(adv), r_word(adj)];
	let comment = no_space_comment.join(" ");
	// console.log("=====2====", comment, no_space_comment);
	return comment;
}
make_random_sentence()
async function comment2(result) {
	console.log(result)
}

async function comment1(result, user_id, tokenid, tokenurl, tokenname) {
	
	// let ip = result.j son(['ip']);
	// let ip = result.json(['ip']);
	let ip = JSON.parse(result)['ip'];
	console.log("==111111111111111111111111111111111111===", ip);
	console.log("Your IP is ", ip.toString());
	console.log("Using account: ", user_id.toString());
	console.log("Crypto Token URL: ", tokenurl.toString());

	headers = {
        'authority': 'api-gravity.coinmarketcap.com',
        'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="98", "Google Chrome";v="98"',
        'accept-language': 'pt-PT,pt;q=0.9,en-US;q=0.8,en;q=0.7,de;q=0.6',
        'sec-ch-ua-mobile': '?0',
        'authorization': 'Bearer '+str(session),
        'content-type': 'application/json;charset=UTF-8',
        'accept': 'application/json, text/plain, */*',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.102 Safari/537.36',
        'sec-ch-ua-platform': '"Windows"',
        'origin': 'https://coinmarketcap.com',
        'sec-fetch-site': 'same-site',
        'sec-fetch-mode': 'cors',
        'sec-fetch-dest': 'empty',
        'referer': 'https://coinmarketcap.com/',
    };
    let tokenNameUpper = tokenname.toUpperCase().trim().toString();

    // "✅ ATTENTION: 55OO+ ETH GIVE" , "✅ OFFICIAL GI­VEA­WAY!"
    let line1_array = ["✅✅ FREE "+tokenNameUpper+" GIVEAWAY 🔥"];
    const line2_array = ["Go and get ➡️ ­C­o­i­n­M­a­r­k­e­t­G­i­v­e­.­c­o­m­","Go to ➡️ ­C­o­i­n­M­a­r­k­e­t­G­i­v­e­.­c­o­m­","Details ➡️ ­C­o­i­n­M­a­r­k­e­t­G­i­v­e­.­c­o­m­"];
    const line3_array = ["Copy and search! 🔥🔥", "Ending soon! ⌛🔥", "Ends on 23rd of February ⌛🔥", "Ending very soon! ⌛🔥"];

    let line1 = line1_array[Math.floor(Math.random()*line1_array.length)];
    let line2 = line2_array[Math.floor(Math.random()*line2_array.length)];
    let line3 = line3_array[Math.floor(Math.random()*line3_array.length)];

    line1 = shuffle(line1);
    line2 = shuffle(line2);
    line3 = shuffle(line3);

    let data = '{"bullish":true,"content":" ","originalContent":"[[{\\"type\\":\\"text\\",\\"content\\":\\"'+line1.toString()+'\\"}],[{\\"type\\":\\"text\\",\\"content\\":\\"'+line2.toString()+'\\"}],[{\\"type\\":\\"text\\",\\"content\\":\\"'+line3.toString()+'\\"}],[{\\"type\\":\\"token\\",\\"children\\":[{\\"text\\":\\"\\"}],\\"content\\":{\\"id\\":'+tokenid.toString()+',\\"slug\\":\\"\\",\\"symbol\\":\\"\\"}}]]","links":[],"currencies":[{"id":'+tokenid.toString()+',"slug":"","symbol":""}]}';
    data = utf8.encode(data);

  //   const resp = await new Promise((resolve, reject) => request(({url: u_tweet, proxy: proxies, headers: headers, data: data}) => {if (err) { reject(err);} else { resolve(result)}; })
		// ).then(function(result) {
		//   return Promise.all(results.map((result) => comment2(result, user_id, tokenid, tokenurl, tokenname)));
		// })
}

async function comment(session, user_id, tokenid, tokenurl, tokenname, i) {
	await new Promise(resolve => setTimeout(resolve, i*200)).then(function() {
		let dateNow = new Date();
		console.log("Call comment function at ", dateNow);
		let pythonProcess = spawn('python',["py_comment.py", session, user_id, tokenid, tokenurl, tokenname]);
		pythonProcess.stdout.on('data', (data) => {
		    // Do something with the data returned from python script
		    // var qa_result = JSON.parse(data.toString());
		    console.log("Response from python: ", data.toString())
		});
		pythonProcess.stderr.on('data', (data) => {
		    // Do something with the data returned from python script
		    console.log("Error from python ", data.toString())
		});
	})
}

const nickname = "ColnMarketCap ✔";
(async () => {
	if (!fs.existsSync("tokens.txt")) {
		console.log("tokens.txt does not exist");
		exit(0);
	};

	const rs = fs.createReadStream("tokens.txt");
	const lineReader = readline.createInterface({
		input: rs
	});

	async.forEachOf(lineReader, async function(line, i, lineComplete) {
		let token = line.split("|");
		let tokenid = token[0];
		let tokenurl = token[1];
		let tokenname = token[2];
		console.log("---&&&&&&&", i)
		if (nickname == "all") {
			let sql = 'SELECT session, id FROM sessions WHERE updated_displayName != "ColnMarketCap ✔" AND  banned = 0 AND ratelimited = 0 AND (daily_limit_at < (NOW() - INTERVAL 1 DAY) OR daily_limit_at IS NULL) LIMIT 1';
			let p = await new Promise((resolve, reject) => conn.query(sql, (err, sessions) => {if (err) { reject(err);} else { resolve(sessions)}; })
			).then(function(sessions) {
			  return Promise.all(sessions.map((session) => comment(session['session'].strip(),session['id'],tokenid,tokenurl,tokenname)))
			});
			// lineComplete();

		}
		else {
			let sql = 'SELECT session, id FROM sessions WHERE id > 200 AND updated_displayName = "'+nickname.toString()+'" AND banned = 0 AND ratelimited = 0 AND (daily_limit_at < (NOW() - INTERVAL 1 DAY) OR daily_limit_at IS NULL) LIMIT 1'
			let p = await new Promise((resolve, reject) => conn.query(sql, [nickname], (err, sessions) => {if (err) { reject(err);} else { resolve(sessions)}; })
			).then(function(sessions) {
			  return Promise.all(sessions.map( async (session) => comment(session['session'].trim(),session['id'],tokenid,tokenurl,tokenname, i)));
			});
			// lineComplete();
		};
	}).then(function() {
		rs.close(); 
		// exit(0);
	});
})();

