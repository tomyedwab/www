.PHONY:

build: .PHONY
	python build/main.py build

dev: .PHONY
	python build/main.py dev

deploy-test: build
	aws s3 sync ./blog/dist s3://test-arguingwithalgorithms-com/
	aws cloudfront create-invalidation --distribution-id E3C0VVOQVZ16WG --paths "/*"

deploy: build
	aws s3 sync ./blog/dist s3://www-arguingwithalgorithms-com/
	aws cloudfront create-invalidation --distribution-id E2WF3223JW9X0E --paths "/*"