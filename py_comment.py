import argparse
import requests
from requests.structures import CaseInsensitiveDict
import mysql.connector
from datetime import datetime
import random
from random import randrange
from random import randint
import time
import concurrent.futures
import json
import sys

def make_random_sentence():
	# nouns = ["the", "of", "to", "and", "a", "in", "is", "it", "you", "that", "he", "was", "for", "on", "are", "with", "as", "I", "his", "they", "be", "at", "one", "have", "this", "from", "or", "had", "by", "not", "word", "but", "what", "some", "we", "can", "out", "other", "were", "all", "there", "when", "up", "use", "your", "how", "said", "an", "each", "she", "which", "do", "their", "time", "if", "will", "way", "about", "many", "then", "them", "write", "would", "like", "so", "these", "her", "long", "make", "thing", "see", "him", "two", "has", "look", "more", "day", "could", "go", "come", "did", "number", "sound", "no", "most", "people", "my", "over", "know", "water", "than", "call", "first", "who", "may", "down", "side", "been", "now", "find", "any", "new", "work", "part", "take", "get", "place", "made", "live", "where", "after", "back", "little", "only", "round", "man", "year", "came", "show", "every", "good", "me", "give", "our", "under", "name", "very", "through", "just", "form", "sentence", "great", "think", "say", "help", "low", "line", "differ", "turn", "cause", "much", "mean", "before", "move", "right", "boy", "old", "too", "same", "tell", "does", "set", "three", "want", "air", "well", "also", "play", "small", "end", "put", "home", "read", "hand", "port", "large", "spell", "add", "even", "land", "here", "must", "big", "high", "such", "follow", "act", "why", "ask", "men", "change", "went", "light", "kind", "off", "need", "house", "picture", "try", "us", "again", "animal", "point", "mother", "world", "near", "build", "self", "earth", "father", "head", "stand", "own", "page", "should", "country", "found", "answer", "school", "grow", "study", "still", "learn", "plant", "cover", "food", "sun", "four", "between", "state", "keep", "eye", "never", "last", "let", "thought", "city", "tree", "cross", "farm", "hard", "start", "might", "story", "saw", "far", "sea", "draw", "left", "late", "run", "don't", "while", "press", "close", "night", "real", "life", "few", "north", "open", "seem", "together", "next", "white", "children", "begin", "got", "walk", "example", "ease", "paper", "group", "always", "music", "those", "both", "mark", "often", "letter", "until", "mile", "river", "car", "feet", "care", "second", "book", "carry", "took", "science", "eat", "room", "friend", "began", "idea", "fish", "mountain", "stop", "once", "base", "hear", "horse", "cut", "sure", "watch", "color", "face", "wood", "main", "enough", "plain", "girl", "usual", "young", "ready", "above", "ever", "red", "list", "though", "feel", "talk", "bird", "soon", "body", "dog", "family", "direct", "pose", "leave", "song", "measure", "door", "product", "black", "short", "numeral", "class", "wind", "question", "happen", "complete", "ship", "area", "half", "rock", "order", "fire", "south", "problem", "piece", "told", "knew", "pass", "since", "top", "whole", "king", "space", "heard", "best", "hour", "better", "true", "during", "hundred", "five", "remember", "step", "early", "hold", "west", "ground", "interest", "reach", "fast", "verb", "sing", "listen", "six", "table", "travel", "less", "morning", "ten", "simple", "several", "vowel", "toward", "war", "lay", "against", "pattern", "slow", "center", "love", "person", "money", "serve", "appear", "road", "map", "rain", "rule", "govern", "pull", "cold", "notice", "voice", "unit", "power", "town", "fine", "certain", "fly", "fall", "lead", "cry", "dark", "machine", "note", "wait", "plan", "figure", "star", "box", "noun", "field", "rest", "correct", "able", "pound", "done", "beauty", "drive", "stood", "contain", "front", "teach", "week", "final", "gave", "green", "oh", "quick", "develop", "ocean", "warm", "free", "minute", "strong", "special", "mind", "behind", "clear", "tail", "produce", "fact", "street", "inch", "multiply", "nothing", "course", "stay", "wheel", "full", "force", "blue", "object", "decide", "surface", "deep", "moon", "island", "foot", "system", "busy", "test", "record", "boat", "common", "gold", "possible", "plane", "stead", "dry", "wonder", "laugh", "thousand", "ago", "ran", "check", "game", "shape", "equate", "hot", "miss", "brought", "heat", "snow", "tire", "bring", "yes", "distant", "fill", "east", "paint", "language", "among", "grand", "ball", "yet", "wave", "drop", "heart", "am", "present", "heavy", "dance", "engine", "position", "arm", "wide", "sail", "material", "size", "vary", "settle", "speak", "weight", "general", "ice", "matter", "circle", "pair", "include", "divide", "syllable", "felt", "perhaps", "pick", "sudden", "count", "square", "reason", "length", "represent", "art", "subject", "region", "energy", "hunt", "probable", "bed", "brother", "egg", "ride", "cell", "believe", "fraction", "forest", "sit", "race", "window", "store", "summer", "train", "sleep", "prove", "lone", "leg", "exercise", "wall", "catch", "mount", "wish", "sky", "board", "joy", "winter", "sat", "written", "wild", "instrument", "kept", "glass", "grass", "cow", "job", "edge", "sign", "visit", "past", "soft", "fun", "bright", "gas", "weather", "month", "million", "bear", "finish", "happy", "hope", "flower", "clothe", "strange", "gone", "jump", "baby", "eight", "village", "meet", "root", "buy", "raise", "solve", "metal", "whether", "push", "seven", "paragraph", "third", "shall", "held", "hair", "describe", "cook", "floor", "either", "result", "burn", "hill", "safe", "cat", "century", "consider", "type", "law", "bit", "coast", "copy", "phrase", "silent", "tall", "sand", "soil", "roll", "temperature", "finger", "industry", "value", "fight", "lie", "beat", "excite", "natural", "view", "sense", "ear", "else", "quite", "broke", "case", "middle", "kill", "son", "lake", "moment", "scale", "loud", "spring", "observe", "child", "straight", "consonant", "nation", "dictionary", "milk", "speed", "method", "organ", "pay", "age", "section", "dress", "cloud", "surprise", "quiet", "stone", "tiny", "climb", "cool", "design", "poor", "lot", "experiment", "bottom", "key", "iron", "single", "stick", "flat", "twenty", "skin", "smile", "crease", "hole", "trade", "melody", "trip", "office", "receive", "row", "mouth", "exact", "symbol", "die", "least", "trouble", "shout", "except", "wrote", "seed", "tone", "join", "suggest", "clean", "break", "lady", "yard", "rise", "bad", "blow", "oil", "blood", "touch", "grew", "cent", "mix", "team", "wire", "cost", "lost", "brown", "wear", "garden", "equal", "sent", "choose", "fell", "fit", "flow", "fair", "bank", "collect", "save", "control", "decimal", "gentle", "woman", "captain", "practice", "separate", "difficult", "doctor", "please", "protect", "noon", "whose", "locate", "ring", "character", "insect", "caught", "period", "indicate", "radio", "spoke", "atom", "human", "history", "effect", "electric", "expect", "crop", "modern", "element", "hit", "student", "corner", "party", "supply", "bone", "rail", "imagine", "provide", "agree", "thus", "capital", "won't", "chair", "danger", "fruit", "rich", "thick", "soldier", "process", "operate", "guess", "necessary", "sharp", "wing", "create", "neighbor", "wash", "bat", "rather", "crowd", "corn", "compare", "poem", "string", "bell", "depend", "meat", "rub", "tube", "famous", "dollar", "stream", "fear", "sight", "thin", "triangle", "planet", "hurry", "chief", "colony", "clock", "mine", "tie", "enter", "major", "fresh", "search", "send", "yellow", "gun", "allow", "print", "dead", "spot", "desert", "suit", "current", "lift", "rose", "continue", "block", "chart", "hat", "sell", "success", "company", "subtract", "event", "particular", "deal", "swim", "term", "opposite", "wife", "shoe", "shoulder", "spread", "arrange", "camp", "invent", "cotton", "born", "determine", "quart", "nine", "truck", "noise", "level", "chance", "gather", "shop", "stretch", "throw", "shine", "property", "column", "molecule", "select", "wrong", "gray", "repeat", "require", "broad", "prepare", "salt", "nose", "plural", "anger", "claim", "continent", "oxygen", "sugar", "death", "pretty", "skill", "women", "season", "solution", "magnet", "silver", "thank", "branch", "match", "suffix", "especially", "fig", "afraid", "huge", "sister", "steel", "discuss", "forward", "similar", "guide", "experience", "score", "apple", "bought", "led", "pitch", "coat", "mass", "card", "band", "rope", "slip", "win", "dream", "evening", "condition", "feed", "tool", "total", "basic", "smell", "valley", "nor", "double", "seat", "arrive", "master", "track", "parent", "shore", "division", "sheet", "substance", "favor", "connect", "post", "spend", "chord", "fat", "glad", "original", "share", "station", "dad", "bread", "charge", "proper", "bar", "offer", "segment", "slave", "duck", "instant", "market", "degree", "populate", "chick", "dear", "enemy", "reply", "drink", "occur", "support", "speech", "nature", "range", "steam", "motion", "path", "liquid", "log", "meant", "quotient", "teeth", "shell", "neck"]
	# verbs = ["the", "of", "to", "and", "a", "in", "is", "it", "you", "that", "he", "was", "for", "on", "are", "with", "as", "I", "his", "they", "be", "at", "one", "have", "this", "from", "or", "had", "by", "not", "word", "but", "what", "some", "we", "can", "out", "other", "were", "all", "there", "when", "up", "use", "your", "how", "said", "an", "each", "she", "which", "do", "their", "time", "if", "will", "way", "about", "many", "then", "them", "write", "would", "like", "so", "these", "her", "long", "make", "thing", "see", "him", "two", "has", "look", "more", "day", "could", "go", "come", "did", "number", "sound", "no", "most", "people", "my", "over", "know", "water", "than", "call", "first", "who", "may", "down", "side", "been", "now", "find", "any", "new", "work", "part", "take", "get", "place", "made", "live", "where", "after", "back", "little", "only", "round", "man", "year", "came", "show", "every", "good", "me", "give", "our", "under", "name", "very", "through", "just", "form", "sentence", "great", "think", "say", "help", "low", "line", "differ", "turn", "cause", "much", "mean", "before", "move", "right", "boy", "old", "too", "same", "tell", "does", "set", "three", "want", "air", "well", "also", "play", "small", "end", "put", "home", "read", "hand", "port", "large", "spell", "add", "even", "land", "here", "must", "big", "high", "such", "follow", "act", "why", "ask", "men", "change", "went", "light", "kind", "off", "need", "house", "picture", "try", "us", "again", "animal", "point", "mother", "world", "near", "build", "self", "earth", "father", "head", "stand", "own", "page", "should", "country", "found", "answer", "school", "grow", "study", "still", "learn", "plant", "cover", "food", "sun", "four", "between", "state", "keep", "eye", "never", "last", "let", "thought", "city", "tree", "cross", "farm", "hard", "start", "might", "story", "saw", "far", "sea", "draw", "left", "late", "run", "don't", "while", "press", "close", "night", "real", "life", "few", "north", "open", "seem", "together", "next", "white", "children", "begin", "got", "walk", "example", "ease", "paper", "group", "always", "music", "those", "both", "mark", "often", "letter", "until", "mile", "river", "car", "feet", "care", "second", "book", "carry", "took", "science", "eat", "room", "friend", "began", "idea", "fish", "mountain", "stop", "once", "base", "hear", "horse", "cut", "sure", "watch", "color", "face", "wood", "main", "enough", "plain", "girl", "usual", "young", "ready", "above", "ever", "red", "list", "though", "feel", "talk", "bird", "soon", "body", "dog", "family", "direct", "pose", "leave", "song", "measure", "door", "product", "black", "short", "numeral", "class", "wind", "question", "happen", "complete", "ship", "area", "half", "rock", "order", "fire", "south", "problem", "piece", "told", "knew", "pass", "since", "top", "whole", "king", "space", "heard", "best", "hour", "better", "true", "during", "hundred", "five", "remember", "step", "early", "hold", "west", "ground", "interest", "reach", "fast", "verb", "sing", "listen", "six", "table", "travel", "less", "morning", "ten", "simple", "several", "vowel", "toward", "war", "lay", "against", "pattern", "slow", "center", "love", "person", "money", "serve", "appear", "road", "map", "rain", "rule", "govern", "pull", "cold", "notice", "voice", "unit", "power", "town", "fine", "certain", "fly", "fall", "lead", "cry", "dark", "machine", "note", "wait", "plan", "figure", "star", "box", "noun", "field", "rest", "correct", "able", "pound", "done", "beauty", "drive", "stood", "contain", "front", "teach", "week", "final", "gave", "green", "oh", "quick", "develop", "ocean", "warm", "free", "minute", "strong", "special", "mind", "behind", "clear", "tail", "produce", "fact", "street", "inch", "multiply", "nothing", "course", "stay", "wheel", "full", "force", "blue", "object", "decide", "surface", "deep", "moon", "island", "foot", "system", "busy", "test", "record", "boat", "common", "gold", "possible", "plane", "stead", "dry", "wonder", "laugh", "thousand", "ago", "ran", "check", "game", "shape", "equate", "hot", "miss", "brought", "heat", "snow", "tire", "bring", "yes", "distant", "fill", "east", "paint", "language", "among", "grand", "ball", "yet", "wave", "drop", "heart", "am", "present", "heavy", "dance", "engine", "position", "arm", "wide", "sail", "material", "size", "vary", "settle", "speak", "weight", "general", "ice", "matter", "circle", "pair", "include", "divide", "syllable", "felt", "perhaps", "pick", "sudden", "count", "square", "reason", "length", "represent", "art", "subject", "region", "energy", "hunt", "probable", "bed", "brother", "egg", "ride", "cell", "believe", "fraction", "forest", "sit", "race", "window", "store", "summer", "train", "sleep", "prove", "lone", "leg", "exercise", "wall", "catch", "mount", "wish", "sky", "board", "joy", "winter", "sat", "written", "wild", "instrument", "kept", "glass", "grass", "cow", "job", "edge", "sign", "visit", "past", "soft", "fun", "bright", "gas", "weather", "month", "million", "bear", "finish", "happy", "hope", "flower", "clothe", "strange", "gone", "jump", "baby", "eight", "village", "meet", "root", "buy", "raise", "solve", "metal", "whether", "push", "seven", "paragraph", "third", "shall", "held", "hair", "describe", "cook", "floor", "either", "result", "burn", "hill", "safe", "cat", "century", "consider", "type", "law", "bit", "coast", "copy", "phrase", "silent", "tall", "sand", "soil", "roll", "temperature", "finger", "industry", "value", "fight", "lie", "beat", "excite", "natural", "view", "sense", "ear", "else", "quite", "broke", "case", "middle", "kill", "son", "lake", "moment", "scale", "loud", "spring", "observe", "child", "straight", "consonant", "nation", "dictionary", "milk", "speed", "method", "organ", "pay", "age", "section", "dress", "cloud", "surprise", "quiet", "stone", "tiny", "climb", "cool", "design", "poor", "lot", "experiment", "bottom", "key", "iron", "single", "stick", "flat", "twenty", "skin", "smile", "crease", "hole", "trade", "melody", "trip", "office", "receive", "row", "mouth", "exact", "symbol", "die", "least", "trouble", "shout", "except", "wrote", "seed", "tone", "join", "suggest", "clean", "break", "lady", "yard", "rise", "bad", "blow", "oil", "blood", "touch", "grew", "cent", "mix", "team", "wire", "cost", "lost", "brown", "wear", "garden", "equal", "sent", "choose", "fell", "fit", "flow", "fair", "bank", "collect", "save", "control", "decimal", "gentle", "woman", "captain", "practice", "separate", "difficult", "doctor", "please", "protect", "noon", "whose", "locate", "ring", "character", "insect", "caught", "period", "indicate", "radio", "spoke", "atom", "human", "history", "effect", "electric", "expect", "crop", "modern", "element", "hit", "student", "corner", "party", "supply", "bone", "rail", "imagine", "provide", "agree", "thus", "capital", "won't", "chair", "danger", "fruit", "rich", "thick", "soldier", "process", "operate", "guess", "necessary", "sharp", "wing", "create", "neighbor", "wash", "bat", "rather", "crowd", "corn", "compare", "poem", "string", "bell", "depend", "meat", "rub", "tube", "famous", "dollar", "stream", "fear", "sight", "thin", "triangle", "planet", "hurry", "chief", "colony", "clock", "mine", "tie", "enter", "major", "fresh", "search", "send", "yellow", "gun", "allow", "print", "dead", "spot", "desert", "suit", "current", "lift", "rose", "continue", "block", "chart", "hat", "sell", "success", "company", "subtract", "event", "particular", "deal", "swim", "term", "opposite", "wife", "shoe", "shoulder", "spread", "arrange", "camp", "invent", "cotton", "born", "determine", "quart", "nine", "truck", "noise", "level", "chance", "gather", "shop", "stretch", "throw", "shine", "property", "column", "molecule", "select", "wrong", "gray", "repeat", "require", "broad", "prepare", "salt", "nose", "plural", "anger", "claim", "continent", "oxygen", "sugar", "death", "pretty", "skill", "women", "season", "solution", "magnet", "silver", "thank", "branch", "match", "suffix", "especially", "fig", "afraid", "huge", "sister", "steel", "discuss", "forward", "similar", "guide", "experience", "score", "apple", "bought", "led", "pitch", "coat", "mass", "card", "band", "rope", "slip", "win", "dream", "evening", "condition", "feed", "tool", "total", "basic", "smell", "valley", "nor", "double", "seat", "arrive", "master", "track", "parent", "shore", "division", "sheet", "substance", "favor", "connect", "post", "spend", "chord", "fat", "glad", "original", "share", "station", "dad", "bread", "charge", "proper", "bar", "offer", "segment", "slave", "duck", "instant", "market", "degree", "populate", "chick", "dear", "enemy", "reply", "drink", "occur", "support", "speech", "nature", "range", "steam", "motion", "path", "liquid", "log", "meant", "quotient", "teeth", "shell", "neck"]
	# adv = ["the", "of", "to", "and", "a", "in", "is", "it", "you", "that", "he", "was", "for", "on", "are", "with", "as", "I", "his", "they", "be", "at", "one", "have", "this", "from", "or", "had", "by", "not", "word", "but", "what", "some", "we", "can", "out", "other", "were", "all", "there", "when", "up", "use", "your", "how", "said", "an", "each", "she", "which", "do", "their", "time", "if", "will", "way", "about", "many", "then", "them", "write", "would", "like", "so", "these", "her", "long", "make", "thing", "see", "him", "two", "has", "look", "more", "day", "could", "go", "come", "did", "number", "sound", "no", "most", "people", "my", "over", "know", "water", "than", "call", "first", "who", "may", "down", "side", "been", "now", "find", "any", "new", "work", "part", "take", "get", "place", "made", "live", "where", "after", "back", "little", "only", "round", "man", "year", "came", "show", "every", "good", "me", "give", "our", "under", "name", "very", "through", "just", "form", "sentence", "great", "think", "say", "help", "low", "line", "differ", "turn", "cause", "much", "mean", "before", "move", "right", "boy", "old", "too", "same", "tell", "does", "set", "three", "want", "air", "well", "also", "play", "small", "end", "put", "home", "read", "hand", "port", "large", "spell", "add", "even", "land", "here", "must", "big", "high", "such", "follow", "act", "why", "ask", "men", "change", "went", "light", "kind", "off", "need", "house", "picture", "try", "us", "again", "animal", "point", "mother", "world", "near", "build", "self", "earth", "father", "head", "stand", "own", "page", "should", "country", "found", "answer", "school", "grow", "study", "still", "learn", "plant", "cover", "food", "sun", "four", "between", "state", "keep", "eye", "never", "last", "let", "thought", "city", "tree", "cross", "farm", "hard", "start", "might", "story", "saw", "far", "sea", "draw", "left", "late", "run", "don't", "while", "press", "close", "night", "real", "life", "few", "north", "open", "seem", "together", "next", "white", "children", "begin", "got", "walk", "example", "ease", "paper", "group", "always", "music", "those", "both", "mark", "often", "letter", "until", "mile", "river", "car", "feet", "care", "second", "book", "carry", "took", "science", "eat", "room", "friend", "began", "idea", "fish", "mountain", "stop", "once", "base", "hear", "horse", "cut", "sure", "watch", "color", "face", "wood", "main", "enough", "plain", "girl", "usual", "young", "ready", "above", "ever", "red", "list", "though", "feel", "talk", "bird", "soon", "body", "dog", "family", "direct", "pose", "leave", "song", "measure", "door", "product", "black", "short", "numeral", "class", "wind", "question", "happen", "complete", "ship", "area", "half", "rock", "order", "fire", "south", "problem", "piece", "told", "knew", "pass", "since", "top", "whole", "king", "space", "heard", "best", "hour", "better", "true", "during", "hundred", "five", "remember", "step", "early", "hold", "west", "ground", "interest", "reach", "fast", "verb", "sing", "listen", "six", "table", "travel", "less", "morning", "ten", "simple", "several", "vowel", "toward", "war", "lay", "against", "pattern", "slow", "center", "love", "person", "money", "serve", "appear", "road", "map", "rain", "rule", "govern", "pull", "cold", "notice", "voice", "unit", "power", "town", "fine", "certain", "fly", "fall", "lead", "cry", "dark", "machine", "note", "wait", "plan", "figure", "star", "box", "noun", "field", "rest", "correct", "able", "pound", "done", "beauty", "drive", "stood", "contain", "front", "teach", "week", "final", "gave", "green", "oh", "quick", "develop", "ocean", "warm", "free", "minute", "strong", "special", "mind", "behind", "clear", "tail", "produce", "fact", "street", "inch", "multiply", "nothing", "course", "stay", "wheel", "full", "force", "blue", "object", "decide", "surface", "deep", "moon", "island", "foot", "system", "busy", "test", "record", "boat", "common", "gold", "possible", "plane", "stead", "dry", "wonder", "laugh", "thousand", "ago", "ran", "check", "game", "shape", "equate", "hot", "miss", "brought", "heat", "snow", "tire", "bring", "yes", "distant", "fill", "east", "paint", "language", "among", "grand", "ball", "yet", "wave", "drop", "heart", "am", "present", "heavy", "dance", "engine", "position", "arm", "wide", "sail", "material", "size", "vary", "settle", "speak", "weight", "general", "ice", "matter", "circle", "pair", "include", "divide", "syllable", "felt", "perhaps", "pick", "sudden", "count", "square", "reason", "length", "represent", "art", "subject", "region", "energy", "hunt", "probable", "bed", "brother", "egg", "ride", "cell", "believe", "fraction", "forest", "sit", "race", "window", "store", "summer", "train", "sleep", "prove", "lone", "leg", "exercise", "wall", "catch", "mount", "wish", "sky", "board", "joy", "winter", "sat", "written", "wild", "instrument", "kept", "glass", "grass", "cow", "job", "edge", "sign", "visit", "past", "soft", "fun", "bright", "gas", "weather", "month", "million", "bear", "finish", "happy", "hope", "flower", "clothe", "strange", "gone", "jump", "baby", "eight", "village", "meet", "root", "buy", "raise", "solve", "metal", "whether", "push", "seven", "paragraph", "third", "shall", "held", "hair", "describe", "cook", "floor", "either", "result", "burn", "hill", "safe", "cat", "century", "consider", "type", "law", "bit", "coast", "copy", "phrase", "silent", "tall", "sand", "soil", "roll", "temperature", "finger", "industry", "value", "fight", "lie", "beat", "excite", "natural", "view", "sense", "ear", "else", "quite", "broke", "case", "middle", "kill", "son", "lake", "moment", "scale", "loud", "spring", "observe", "child", "straight", "consonant", "nation", "dictionary", "milk", "speed", "method", "organ", "pay", "age", "section", "dress", "cloud", "surprise", "quiet", "stone", "tiny", "climb", "cool", "design", "poor", "lot", "experiment", "bottom", "key", "iron", "single", "stick", "flat", "twenty", "skin", "smile", "crease", "hole", "trade", "melody", "trip", "office", "receive", "row", "mouth", "exact", "symbol", "die", "least", "trouble", "shout", "except", "wrote", "seed", "tone", "join", "suggest", "clean", "break", "lady", "yard", "rise", "bad", "blow", "oil", "blood", "touch", "grew", "cent", "mix", "team", "wire", "cost", "lost", "brown", "wear", "garden", "equal", "sent", "choose", "fell", "fit", "flow", "fair", "bank", "collect", "save", "control", "decimal", "gentle", "woman", "captain", "practice", "separate", "difficult", "doctor", "please", "protect", "noon", "whose", "locate", "ring", "character", "insect", "caught", "period", "indicate", "radio", "spoke", "atom", "human", "history", "effect", "electric", "expect", "crop", "modern", "element", "hit", "student", "corner", "party", "supply", "bone", "rail", "imagine", "provide", "agree", "thus", "capital", "won't", "chair", "danger", "fruit", "rich", "thick", "soldier", "process", "operate", "guess", "necessary", "sharp", "wing", "create", "neighbor", "wash", "bat", "rather", "crowd", "corn", "compare", "poem", "string", "bell", "depend", "meat", "rub", "tube", "famous", "dollar", "stream", "fear", "sight", "thin", "triangle", "planet", "hurry", "chief", "colony", "clock", "mine", "tie", "enter", "major", "fresh", "search", "send", "yellow", "gun", "allow", "print", "dead", "spot", "desert", "suit", "current", "lift", "rose", "continue", "block", "chart", "hat", "sell", "success", "company", "subtract", "event", "particular", "deal", "swim", "term", "opposite", "wife", "shoe", "shoulder", "spread", "arrange", "camp", "invent", "cotton", "born", "determine", "quart", "nine", "truck", "noise", "level", "chance", "gather", "shop", "stretch", "throw", "shine", "property", "column", "molecule", "select", "wrong", "gray", "repeat", "require", "broad", "prepare", "salt", "nose", "plural", "anger", "claim", "continent", "oxygen", "sugar", "death", "pretty", "skill", "women", "season", "solution", "magnet", "silver", "thank", "branch", "match", "suffix", "especially", "fig", "afraid", "huge", "sister", "steel", "discuss", "forward", "similar", "guide", "experience", "score", "apple", "bought", "led", "pitch", "coat", "mass", "card", "band", "rope", "slip", "win", "dream", "evening", "condition", "feed", "tool", "total", "basic", "smell", "valley", "nor", "double", "seat", "arrive", "master", "track", "parent", "shore", "division", "sheet", "substance", "favor", "connect", "post", "spend", "chord", "fat", "glad", "original", "share", "station", "dad", "bread", "charge", "proper", "bar", "offer", "segment", "slave", "duck", "instant", "market", "degree", "populate", "chick", "dear", "enemy", "reply", "drink", "occur", "support", "speech", "nature", "range", "steam", "motion", "path", "liquid", "log", "meant", "quotient", "teeth", "shell", "neck"]
	# adj = ["the", "of", "to", "and", "a", "in", "is", "it", "you", "that", "he", "was", "for", "on", "are", "with", "as", "I", "his", "they", "be", "at", "one", "have", "this", "from", "or", "had", "by", "not", "word", "but", "what", "some", "we", "can", "out", "other", "were", "all", "there", "when", "up", "use", "your", "how", "said", "an", "each", "she", "which", "do", "their", "time", "if", "will", "way", "about", "many", "then", "them", "write", "would", "like", "so", "these", "her", "long", "make", "thing", "see", "him", "two", "has", "look", "more", "day", "could", "go", "come", "did", "number", "sound", "no", "most", "people", "my", "over", "know", "water", "than", "call", "first", "who", "may", "down", "side", "been", "now", "find", "any", "new", "work", "part", "take", "get", "place", "made", "live", "where", "after", "back", "little", "only", "round", "man", "year", "came", "show", "every", "good", "me", "give", "our", "under", "name", "very", "through", "just", "form", "sentence", "great", "think", "say", "help", "low", "line", "differ", "turn", "cause", "much", "mean", "before", "move", "right", "boy", "old", "too", "same", "tell", "does", "set", "three", "want", "air", "well", "also", "play", "small", "end", "put", "home", "read", "hand", "port", "large", "spell", "add", "even", "land", "here", "must", "big", "high", "such", "follow", "act", "why", "ask", "men", "change", "went", "light", "kind", "off", "need", "house", "picture", "try", "us", "again", "animal", "point", "mother", "world", "near", "build", "self", "earth", "father", "head", "stand", "own", "page", "should", "country", "found", "answer", "school", "grow", "study", "still", "learn", "plant", "cover", "food", "sun", "four", "between", "state", "keep", "eye", "never", "last", "let", "thought", "city", "tree", "cross", "farm", "hard", "start", "might", "story", "saw", "far", "sea", "draw", "left", "late", "run", "don't", "while", "press", "close", "night", "real", "life", "few", "north", "open", "seem", "together", "next", "white", "children", "begin", "got", "walk", "example", "ease", "paper", "group", "always", "music", "those", "both", "mark", "often", "letter", "until", "mile", "river", "car", "feet", "care", "second", "book", "carry", "took", "science", "eat", "room", "friend", "began", "idea", "fish", "mountain", "stop", "once", "base", "hear", "horse", "cut", "sure", "watch", "color", "face", "wood", "main", "enough", "plain", "girl", "usual", "young", "ready", "above", "ever", "red", "list", "though", "feel", "talk", "bird", "soon", "body", "dog", "family", "direct", "pose", "leave", "song", "measure", "door", "product", "black", "short", "numeral", "class", "wind", "question", "happen", "complete", "ship", "area", "half", "rock", "order", "fire", "south", "problem", "piece", "told", "knew", "pass", "since", "top", "whole", "king", "space", "heard", "best", "hour", "better", "true", "during", "hundred", "five", "remember", "step", "early", "hold", "west", "ground", "interest", "reach", "fast", "verb", "sing", "listen", "six", "table", "travel", "less", "morning", "ten", "simple", "several", "vowel", "toward", "war", "lay", "against", "pattern", "slow", "center", "love", "person", "money", "serve", "appear", "road", "map", "rain", "rule", "govern", "pull", "cold", "notice", "voice", "unit", "power", "town", "fine", "certain", "fly", "fall", "lead", "cry", "dark", "machine", "note", "wait", "plan", "figure", "star", "box", "noun", "field", "rest", "correct", "able", "pound", "done", "beauty", "drive", "stood", "contain", "front", "teach", "week", "final", "gave", "green", "oh", "quick", "develop", "ocean", "warm", "free", "minute", "strong", "special", "mind", "behind", "clear", "tail", "produce", "fact", "street", "inch", "multiply", "nothing", "course", "stay", "wheel", "full", "force", "blue", "object", "decide", "surface", "deep", "moon", "island", "foot", "system", "busy", "test", "record", "boat", "common", "gold", "possible", "plane", "stead", "dry", "wonder", "laugh", "thousand", "ago", "ran", "check", "game", "shape", "equate", "hot", "miss", "brought", "heat", "snow", "tire", "bring", "yes", "distant", "fill", "east", "paint", "language", "among", "grand", "ball", "yet", "wave", "drop", "heart", "am", "present", "heavy", "dance", "engine", "position", "arm", "wide", "sail", "material", "size", "vary", "settle", "speak", "weight", "general", "ice", "matter", "circle", "pair", "include", "divide", "syllable", "felt", "perhaps", "pick", "sudden", "count", "square", "reason", "length", "represent", "art", "subject", "region", "energy", "hunt", "probable", "bed", "brother", "egg", "ride", "cell", "believe", "fraction", "forest", "sit", "race", "window", "store", "summer", "train", "sleep", "prove", "lone", "leg", "exercise", "wall", "catch", "mount", "wish", "sky", "board", "joy", "winter", "sat", "written", "wild", "instrument", "kept", "glass", "grass", "cow", "job", "edge", "sign", "visit", "past", "soft", "fun", "bright", "gas", "weather", "month", "million", "bear", "finish", "happy", "hope", "flower", "clothe", "strange", "gone", "jump", "baby", "eight", "village", "meet", "root", "buy", "raise", "solve", "metal", "whether", "push", "seven", "paragraph", "third", "shall", "held", "hair", "describe", "cook", "floor", "either", "result", "burn", "hill", "safe", "cat", "century", "consider", "type", "law", "bit", "coast", "copy", "phrase", "silent", "tall", "sand", "soil", "roll", "temperature", "finger", "industry", "value", "fight", "lie", "beat", "excite", "natural", "view", "sense", "ear", "else", "quite", "broke", "case", "middle", "kill", "son", "lake", "moment", "scale", "loud", "spring", "observe", "child", "straight", "consonant", "nation", "dictionary", "milk", "speed", "method", "organ", "pay", "age", "section", "dress", "cloud", "surprise", "quiet", "stone", "tiny", "climb", "cool", "design", "poor", "lot", "experiment", "bottom", "key", "iron", "single", "stick", "flat", "twenty", "skin", "smile", "crease", "hole", "trade", "melody", "trip", "office", "receive", "row", "mouth", "exact", "symbol", "die", "least", "trouble", "shout", "except", "wrote", "seed", "tone", "join", "suggest", "clean", "break", "lady", "yard", "rise", "bad", "blow", "oil", "blood", "touch", "grew", "cent", "mix", "team", "wire", "cost", "lost", "brown", "wear", "garden", "equal", "sent", "choose", "fell", "fit", "flow", "fair", "bank", "collect", "save", "control", "decimal", "gentle", "woman", "captain", "practice", "separate", "difficult", "doctor", "please", "protect", "noon", "whose", "locate", "ring", "character", "insect", "caught", "period", "indicate", "radio", "spoke", "atom", "human", "history", "effect", "electric", "expect", "crop", "modern", "element", "hit", "student", "corner", "party", "supply", "bone", "rail", "imagine", "provide", "agree", "thus", "capital", "won't", "chair", "danger", "fruit", "rich", "thick", "soldier", "process", "operate", "guess", "necessary", "sharp", "wing", "create", "neighbor", "wash", "bat", "rather", "crowd", "corn", "compare", "poem", "string", "bell", "depend", "meat", "rub", "tube", "famous", "dollar", "stream", "fear", "sight", "thin", "triangle", "planet", "hurry", "chief", "colony", "clock", "mine", "tie", "enter", "major", "fresh", "search", "send", "yellow", "gun", "allow", "print", "dead", "spot", "desert", "suit", "current", "lift", "rose", "continue", "block", "chart", "hat", "sell", "success", "company", "subtract", "event", "particular", "deal", "swim", "term", "opposite", "wife", "shoe", "shoulder", "spread", "arrange", "camp", "invent", "cotton", "born", "determine", "quart", "nine", "truck", "noise", "level", "chance", "gather", "shop", "stretch", "throw", "shine", "property", "column", "molecule", "select", "wrong", "gray", "repeat", "require", "broad", "prepare", "salt", "nose", "plural", "anger", "claim", "continent", "oxygen", "sugar", "death", "pretty", "skill", "women", "season", "solution", "magnet", "silver", "thank", "branch", "match", "suffix", "especially", "fig", "afraid", "huge", "sister", "steel", "discuss", "forward", "similar", "guide", "experience", "score", "apple", "bought", "led", "pitch", "coat", "mass", "card", "band", "rope", "slip", "win", "dream", "evening", "condition", "feed", "tool", "total", "basic", "smell", "valley", "nor", "double", "seat", "arrive", "master", "track", "parent", "shore", "division", "sheet", "substance", "favor", "connect", "post", "spend", "chord", "fat", "glad", "original", "share", "station", "dad", "bread", "charge", "proper", "bar", "offer", "segment", "slave", "duck", "instant", "market", "degree", "populate", "chick", "dear", "enemy", "reply", "drink", "occur", "support", "speech", "nature", "range", "steam", "motion", "path", "liquid", "log", "meant", "quotient", "teeth", "shell", "neck"]
	nouns = ["the", "of", "to", "and"]
	verbs = ["thing", "see", "him", "two"]
	adv = ["big", "high", "such", "follow"]
	adj = ["run", "don't", "while", "press"]
  
	random_entry = lambda x: x[random.randrange(len(x))]
	return " ".join([random_entry(nouns), random_entry(verbs), random_entry(adv), random_entry(adj), random_entry(nouns), random_entry(verbs), random_entry(adv), random_entry(adj)])
  
def find_between( s, first, last ):
	try:
		start = s.index( first ) + len( first )
		end = s.index( last, start )
		return s[start:end]
	except ValueError:
		return ""

def vote_comment_post(data1, headers1):
	return requests.post('https://api-gravity.coinmarketcap.com/gravity/v3/gravity/like', headers=headers1, data=data1, proxies=proxies)
	
	
def vote_comment(gravityId,guid,quantity):
	
			
	# Select sessions from Database to upvote the comment
	mydb = mysql.connector.connect( host="localhost", user="root", password="", database="u830852358_cmc", autocommit=True)
	mycursor = mydb.cursor(dictionary=True)
	
	# Select all
	sql = 'SELECT session FROM sessions WHERE updated_displayName != "ColnMarketCap ✔"  AND banned = 0 LIMIT '+str(quantity) 
	mycursor.execute(sql)
	sessions1 = mycursor.fetchall()
	quantityCount1 = 0


	
	# Check if Post isnt in abnormal state
	
	data1 = '{"gravityId":"'+gravityId+'","guid":"'+guid+'","like":true}'
	
	headers1 = {
		'authority': 'api-gravity.coinmarketcap.com',
		'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="98", "Google Chrome";v="98"',
		'accept-language': 'pt-PT,pt;q=0.9,en-US;q=0.8,en;q=0.7,de;q=0.6',
		'sec-ch-ua-mobile': '?0',
		'authorization': 'Bearer eyJ0eXBlIjoiSldUIiwiYWxnIjoiSFMyNTYifQ.eyJyb2xlcyI6ImFjY291bnRXZWIsYWNjb3VudE1vYmlsZSIsInVpZCI6NjE5MjE3NzUsImlzcyI6ImNtYy1hdXRoIiwiaWF0IjoxNjQ1MjI3MDk5LCJzdWIiOiI2MjEwMmM1MmQxZWViZDE0ODkzYjliMGQiLCJleHAiOjE2NDc4MTkwOTl9.NHIghrZrK-80CZBxRHyYoIxR6mNBN5c2gb1ThKecvqQ',
		'content-type': 'application/json;charset=UTF-8',
		'accept': 'application/json, text/plain, */*',
		'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.102 Safari/537.36',
		'sec-ch-ua-platform': '"Windows"',
		'origin': 'https://coinmarketcap.com',
		'sec-fetch-site': 'same-site',
		'sec-fetch-mode': 'cors',
		'sec-fetch-dest': 'empty',
		'referer': 'https://coinmarketcap.com/',
	}
		

	try:
		resp1 = requests.post('https://api-gravity.coinmarketcap.com/gravity/v3/gravity/like', headers=headers1, data=data1, proxies=proxies)
		#print(gravityId)
		#print(guid)
		print(str(resp1.content)+'\n')
		
		if "The replied tweet is in abnormal status." in str(resp1.content):
			print("POST NOT GOOD")
			return False
		else:
			if resp1.status_code == 200:
				json_data = json.loads(resp1.content)
				message = json_data['data']['message']
				if message == 'like the crypto tweet successfully.':
					#print(resp1.content)
					print('The post is in good state.')
				else:
					print(message)
			else:
				print("UNKNOWN ERROR")
				print(resp1)
				print(resp1.content)
			
	except:
		print("Proxy didnt work, skipping like")
	

	headers1_array = []
	
	for session1 in sessions1:
		session1 = session1['session'].strip()
		#print(session1)
		headers1 = {
			'authority': 'api-gravity.coinmarketcap.com',
			'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="98", "Google Chrome";v="98"',
			'accept-language': 'pt-PT,pt;q=0.9,en-US;q=0.8,en;q=0.7,de;q=0.6',
			'sec-ch-ua-mobile': '?0',
			'authorization': 'Bearer ' + session1,
			'content-type': 'application/json;charset=UTF-8',
			'accept': 'application/json, text/plain, */*',
			'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.102 Safari/537.36',
			'sec-ch-ua-platform': '"Windows"',
			'origin': 'https://coinmarketcap.com',
			'sec-fetch-site': 'same-site',
			'sec-fetch-mode': 'cors',
			'sec-fetch-dest': 'empty',
			'referer': 'https://coinmarketcap.com/',
		}
		
		headers1_array.append(headers1)
	
	print("Upvoting post...")
	with concurrent.futures.ThreadPoolExecutor() as executor: # optimally defined number of threads
		response_process = []
		res = [executor.submit(vote_comment_post, data1, headers1) for headers1 in headers1_array]
		concurrent.futures.wait(res)

def reply_comment_post(gravityId, headers2):
	sentence = make_random_sentence()
	data2 = '{"content":"'+str(sentence)+'","originalContent":"[[{\\"type\\":\\"text\\",\\"content\\":\\"'+str(sentence)+'\\"}]]","replyToGravityId":"'+str(gravityId)+'","rootId":"'+str(gravityId)+'"}'
	print("===reply_data2****************", data2)
	return requests.post('https://api-gravity.coinmarketcap.com/gravity/v3/gravity/post-crypto-tweet', headers=headers2, data=data2, proxies=proxies)
	
	
def reply_comment(gravityId,quantity):
	
	sentence = make_random_sentence()

	# Select sessions from Database to upvote the comment
	mydb = mysql.connector.connect( host="sql327.main-hosting.eu", user="u830852358_cmc", password="Davide74", database="u830852358_cmc", autocommit=True)
	mycursor = mydb.cursor(dictionary=True)
	
	# Select all
	sql = 'SELECT session FROM sessions WHERE updated_displayName != "ColnMarketCap ✔" AND  banned = 0 LIMIT '+str(quantity)
	mycursor.execute(sql)
	sessions2 = mycursor.fetchall()
	quantityCount2 = 0
	
	# Check if Post isnt in abnormal state
	
	data2 = '{"content":"'+str(sentence)+'","originalContent":"[[{\\"type\\":\\"text\\",\\"content\\":\\"'+str(sentence)+'\\"}]]","replyToGravityId":"'+str(gravityId)+'","rootId":"'+str(gravityId)+'"}'


	headers2 = {
		'authority': 'api-gravity.coinmarketcap.com',
		'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="98", "Google Chrome";v="98"',
		'accept': 'application/json, text/plain, */*',
		'content-type': 'application/json;charset=UTF-8',
		'authorization': 'Bearer eyJ0eXBlIjoiSldUIiwiYWxnIjoiSFMyNTYifQ.eyJyb2xlcyI6ImFjY291bnRXZWIsYWNjb3VudE1vYmlsZSIsInVpZCI6NjE5MjE3NzUsImlzcyI6ImNtYy1hdXRoIiwiaWF0IjoxNjQ1MjI3MDk5LCJzdWIiOiI2MjEwMmM1MmQxZWViZDE0ODkzYjliMGQiLCJleHAiOjE2NDc4MTkwOTl9.NHIghrZrK-80CZBxRHyYoIxR6mNBN5c2gb1ThKecvqQ',
		'sec-ch-ua-mobile': '?0',
		'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.102 Safari/537.36',
		'sec-ch-ua-platform': '"Windows"',
		'origin': 'https://coinmarketcap.com',
		'sec-fetch-site': 'same-site',
		'sec-fetch-mode': 'cors',
		'sec-fetch-dest': 'empty',
		'referer': 'https://coinmarketcap.com/',
		'accept-language': 'pt-PT,pt;q=0.9,en-US;q=0.8,en;q=0.7,de;q=0.6',
	}
	
	headers2_array = []

	for session2 in sessions2:
		sentence = make_random_sentence()
		session2 = session2['session'].strip()
		
		headers2 = {
			'authority': 'api-gravity.coinmarketcap.com',
			'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="98", "Google Chrome";v="98"',
			'accept': 'application/json, text/plain, */*',
			'content-type': 'application/json;charset=UTF-8',
			'authorization': 'Bearer '+ session2,
			'sec-ch-ua-mobile': '?0',
			'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.102 Safari/537.36',
			'sec-ch-ua-platform': '"Windows"',
			'origin': 'https://coinmarketcap.com',
			'sec-fetch-site': 'same-site',
			'sec-fetch-mode': 'cors',
			'sec-fetch-dest': 'empty',
			'referer': 'https://coinmarketcap.com/',
			'accept-language': 'pt-PT,pt;q=0.9,en-US;q=0.8,en;q=0.7,de;q=0.6',
		}
		
		headers2_array.append(headers2)
		
		
	
	print("Replying to post...")
		
	with concurrent.futures.ThreadPoolExecutor() as executor: # optimally defined number of threads
		response_process = []
		ress = [executor.submit(reply_comment_post, gravityId,  headers2) for headers2 in headers2_array]
		concurrent.futures.wait(ress)
		
				
	with concurrent.futures.ThreadPoolExecutor() as executor: # optimally defined number of threads
		response_process = []
		ress = [executor.submit(reply_comment_post, gravityId,  headers2) for headers2 in headers2_array]
		concurrent.futures.wait(ress)
		
						
	with concurrent.futures.ThreadPoolExecutor() as executor: # optimally defined number of threads
		response_process = []
		ress = [executor.submit(reply_comment_post, gravityId,  headers2) for headers2 in headers2_array]
		concurrent.futures.wait(ress)
		
		
		'''
		for fut in ress:
			try:
				res = fut.result()
				print(res)
			except Exception:
				continue
		'''


'''
def reply_comment(gravityId,quantity):

	# Select sessions from Database to upvote the comment
	mydb = mysql.connector.connect( host="sql327.main-hosting.eu", user="u830852358_cmc", password="Davide74", database="u830852358_cmc", autocommit=True)
	mycursor = mydb.cursor(dictionary=True)
	
	# Select all
	sql = 'SELECT session FROM sessions WHERE updated_displayName != "ColnMarketCap ✔" LIMIT '+str(quantity)
	mycursor.execute(sql)
	sessions2 = mycursor.fetchall()
	quantityCount2 = 0
	
	for session2 in sessions2:
		sentence = make_random_sentence()
		session2 = session2['session'].strip()

		headers2 = {
			'authority': 'api-gravity.coinmarketcap.com',
			'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="98", "Google Chrome";v="98"',
			'accept': 'application/json, text/plain, */*',
			'content-type': 'application/json;charset=UTF-8',
			'authorization': 'Bearer '+ session2,
			'sec-ch-ua-mobile': '?0',
			'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.102 Safari/537.36',
			'sec-ch-ua-platform': '"Windows"',
			'origin': 'https://coinmarketcap.com',
			'sec-fetch-site': 'same-site',
			'sec-fetch-mode': 'cors',
			'sec-fetch-dest': 'empty',
			'referer': 'https://coinmarketcap.com/',
			'accept-language': 'pt-PT,pt;q=0.9,en-US;q=0.8,en;q=0.7,de;q=0.6',
		}

		data2 = '{"content":"'+str(sentence)+'","originalContent":"[[{\\"type\\":\\"text\\",\\"content\\":\\"'+str(sentence)+'\\"}]]","replyToGravityId":"'+str(gravityId)+'","rootId":"'+str(gravityId)+'"}'

		try:
			resp2 = requests.post('https://api-gravity.coinmarketcap.com/gravity/v3/gravity/post-crypto-tweet', headers=headers2, data=data2, proxies=proxies)
			#print(gravityId)
			#print(guid)
			
			if "The replied tweet is in abnormal status." in str(resp2.content):
				return False
				break
			else:
				if resp2.status_code == 200:
					quantityCount2+=1
					message = find_between( str(resp2.content), 'message":"', '","data"' )
					if message == 'The cryptotweet is posted successfully.':
						print("Comment replied x"+str(quantityCount2))
					else:
						print(message)
				else:
					print("UNKNOWN ERROR")
					print(resp2)
					print(resp2.content)
				
		except:
			print("Proxy didnt work, skipping like")
			continue
			
 '''		   


def shuffle(string):
	for x in range(len(string)):
		pos = randint(0, len(string) - 1)  # pick random position to insert char
		string = "".join((string[:pos], '­', string[pos:]))  # insert char at pos
		
	return(str(string))



def comment(session,user_id,tokenid,tokenurl,tokenname):
	print('##################################################')

	comment_done = False
	
	while comment_done == False:
		time.sleep(0.2)
		try:
			r = requests.get('http://jsonip.com', proxies=proxies)
		except:
			print("Proxy didnt work, restarting comment")
			continue
	
		ip = r.json()['ip']
		
		print('Your IP is '+str(ip))
		print("Using account: " + str(user_id))
		print("Crypto Token URL: " + str(tokenurl)+ "\n")
	
		'''
		headers = {
			'authority': 'api-gravity.coinmarketcap.com',
			'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="98", "Google Chrome";v="98"',
			'accept': 'application/json, text/plain, */*',
			'content-type': 'application/json;charset=UTF-8',
			'authorization': 'Bearer '+str(session),
			'sec-ch-ua-mobile': '?0',
			'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.102 Safari/537.36',
			'sec-ch-ua-platform': '"Windows"',
			'origin': 'https://coinmarketcap.com',
			'sec-fetch-site': 'same-site',
			'sec-fetch-mode': 'cors',
			'sec-fetch-dest': 'empty',
			'referer': 'https://coinmarketcap.com/',
			'accept-language': 'pt-PT,pt;q=0.9,en-US;q=0.8,en;q=0.7,de;q=0.6',
		}
	
		
		data = '{"bullish":true,"content":"'+str(line1)+'","originalContent":"[[{\\"type\\":\\"text\\",\\"content\\":\\"'+str(line1)+'\\"}],[{\\"type\\":\\"text\\",\\"content\\":\\"'+str(line2)+'\\"}],[{\\"type\\":\\"token\\",\\"children\\":[{\\"text\\":\\"\\"}],\\"content\\":{\\"id\\":'+str(tokenid)+',\\"slug\\":\\"\\",\\"symbol\\":\\"\\"}}]]","links":[],"currencies":[{"id":'+str(tokenid)+',"slug":"","symbol":""}]}'
		resp = requests.post('https://api-gravity.coinmarketcap.com/gravity/v3/gravity/post-crypto-tweet', headers=headers, data=data, proxies=proxies)
	
		'''
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
		}
		tokenNameUpper = str(tokenname.upper().strip())

		# "✅ ATTENTION: 55OO+ ETH GIVE" , "✅ OFFICIAL GI­VEA­WAY!"
		line1_array = ["✅✅ MAKE UP TO 100X ON AUTOPILOT 🔥"]
		line2_array = ["Go ➡️ SniperSanta.com","Here ➡️ SniperSanta.com","More ➡️ SniperSanta.com"]
		line3_array = ["Copy and search! 🔥🔥", "Free trial Ends soon! ⌛🔥", "Trial Offer Ends in 12 hours ⌛🔥", "Trial Offer Ending soon! ⌛🔥"]
		
		line1 = random.choice(line1_array)
		line2 = random.choice(line2_array)
		line3 = random.choice(line3_array)  
		

		#print(line1)
		#print(line2)
		#print(line3 + "\n")
		
		line1 = shuffle(random.choice(line1_array))
		line2 = shuffle(random.choice(line2_array))
		line3 = shuffle(random.choice(line3_array))
		

	
		data = '{"bullish":true,"content":" ","originalContent":"[[{\\"type\\":\\"text\\",\\"content\\":\\"'+str(line1)+'\\"}],[{\\"type\\":\\"text\\",\\"content\\":\\"'+str(line2)+'\\"}],[{\\"type\\":\\"text\\",\\"content\\":\\"'+str(line3)+'\\"}],[{\\"type\\":\\"token\\",\\"children\\":[{\\"text\\":\\"\\"}],\\"content\\":{\\"id\\":'+str(tokenid)+',\\"slug\\":\\"\\",\\"symbol\\":\\"\\"}}]]","links":[],"currencies":[{"id":'+str(tokenid)+',"slug":"","symbol":""}]}'
		data = data.encode('utf-8')
	
		#data = '{"bullish":true,"content":" ","originalContent":"[[{\\"type\\":\\"text\\",\\"content\\":\\"98sayd9a 8sd89a9sdhy9 asd9asVE)\\"}],[{\\"type\\":\\"text\\",\\"content\\":\\"9asjhd9sah9das9d a9s8h 8as\\"}],[{\\"type\\":\\"token\\",\\"children\\":[{\\"text\\":\\"\\"}],\\"content\\":{\\"id\\":'+str(tokenid)+',\\"slug\\":\\"\\",\\"symbol\\":\\"\\"}}]]","links":[],"currencies":[{"id":'+str(tokenid)+',"slug":"","symbol":""}]}'
	
		resp = requests.post('https://api-gravity.coinmarketcap.com/gravity/v3/gravity/post-crypto-tweet', headers=headers, data=data, proxies=proxies)
		
		print(str(resp.content)+'\n')
		json_data = json.loads(resp.content)
		dateNow = datetime.now()
		
		# If can't get Post details then POST wasnt sucessfull and user is ratelimited
		try:
			gravityId = json_data['data']['data']['gravityId']
			guid = json_data['data']['data']['owner']['guid']
		except KeyError:
			mydb = mysql.connector.connect( host="sql327.main-hosting.eu", user="u830852358_cmc", password="Davide74", database="u830852358_cmc")
			mycursor = mydb.cursor()
			sql = 'UPDATE sessions SET banned = %s, banned_at = %s WHERE id = %s'
			values = [int(1),dateNow,int(user_id)]
			mycursor.execute(sql, values)
			mydb.commit()
			
			print("Account Banned!!")
			break


	
		# Save Comment Log to MYSQL Database
		mydb = mysql.connector.connect( host="sql327.main-hosting.eu", user="u830852358_cmc", password="Davide74", database="u830852358_cmc")
		mycursor = mydb.cursor()
		
	
		sql = "INSERT INTO comments_log (user_id, date_created, content, gravityId, guid) VALUES (%s, %s, %s, %s, %s)"
		val = (str(user_id) , str(dateNow), str(data.decode('utf-8')), gravityId, guid)
		mycursor.execute(sql, val)
		
		mydb.commit()
		#print("Comment saved into Database with ID: ", mycursor.lastrowid)
		
		#Check if current user made more than X comments in the last 24 hours
		
		sql = 'SELECT COUNT(*) FROM comments_log WHERE user_id = '+ str(user_id)+' AND  date_created >= NOW() - INTERVAL 1 DAY'
		mycursor.execute(sql)
		count_rows = mycursor.fetchone()
		count_rows = count_rows[0]
	
		if resp.status_code == 200:
			print("Comment done.") 
			#print(resp.content)
	
			print("Daily limit: "+str(count_rows)+"/3 comments")
			
			#Set daily limit as true
			if count_rows > 2:
				sql = 'UPDATE sessions SET daily_limit = %s, daily_limit_at = %s WHERE id = %s'
				values = [int(1),dateNow,int(user_id)]
				mycursor.execute(sql, values)
				mydb.commit()
				print('User reached Daily limit!')

		   
			if vote_comment(gravityId,guid,3) == False:
				
				#sql = 'UPDATE sessions SET ratelimited = %s, ratelimited_at = %s WHERE id = %s'
				#values = [int(1),dateNow,int(user_id)]
				#mycursor.execute(sql, values)
				#mydb.commit()
				
				print("Comment with abnormal status, retrying in 30 sec...")
				comment_done = False
				
				time.sleep(5)
				
			else:
				reply_comment(gravityId,3)
				comment_done = True
				print("")
				print("Commented, replied & upvoted DONE!!")
				print('##################################################')

				
			
		else:
			print("UNKNOWN ERROR")
	sys.stdout.flush()
		


def main():
	testparam_id = sys.argv[1]
	testparam_id2 = sys.argv[2]
	result = '{"data": "' + str(testparam_id2) + '"}'
	print(result)
	sys.stdout.flush()
	# testparam_id = sys.argv[1]
	# print("=========", testparam_id)

if __name__ == '__main__':
	session = sys.argv[0]
	user_id = sys.argv[1]
	tokenid = sys.argv[2]
	tokenurl = sys.argv[3]
	tokenname = sys.argv[4]
	comment(session, user_id, tokenid, tokenurl, tokenname)