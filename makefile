default:
	cat Makefile

get_texts:
	@echo "Getting books..."
	/bin/bash get_the_books.sh

raven_line_count: 
	@echo "Line count in The Raven"
	@cat pg17192.txt | wc -l 

raven_word_count:
	@echo "Word count in The Raven"
	@cat pg17192.txt | wc -w

raven_counts: 
	@echo "Lowercase 'raven' count:"
	@cat pg17192.txt | grep 'raven' | wc -l
	@echo "Titlecase 'Raven' count:"
	@cat pg17192.txt | grep 'Raven' | wc -l 
	@echo "Case-insensitive 'raven' count:"
	@cat pg17192.txt | grep -i 'raven' | wc -l

total_lines:
	@cat *.txt | wc -l

total_words:
	@cat *.txt | wc -w

setup: 
	python3 -m venv env
	./env/bin/pip install --upgrade pip 
	./env/bin/pip install -r requirements.txt

test:
	@echo "Running non-integration tests..."
	pytest -v -m "not integration"

clean: 
	@echo "Removing books..."
	rm -rf books/	
