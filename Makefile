.PHONY:

build: .PHONY
	python build/main.py build

dev: .PHONY
	python build/main.py dev

deploy-test: build
	aws s3 sync ./blog/dist s3://test-arguingwithalgorithms-com/

deploy: build
	aws s3 sync ./blog/dist s3://www-arguingwithalgorithms-com/