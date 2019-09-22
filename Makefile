

deploycmd = sls deploy -v --aws-profile perso-adminolive
removecmd = sls remove -v --aws-profile perso-adminolive

servicedir1 = multiple-services/hands-on-1_uploads
servicedir2 = multiple-services/hands-on-2_py-aws-lambda-presigned-url-template
servicedir3 = multiple-services/hands-on-3_and_4_py-aws-lambda-image-reco-template
servicedir5 = multiple-services/hands-on-5_py-aws-lambda-db-save-template
servicedir6 = multiple-services/hands-on-6_py-aws-lambda-db-list-items-template 
servicedir7 = multiple-services/py-aws-lambda-thumbnail-gen-template

deploy: deploy1 deploy2 deploy3 deploy5 deploy6 deploy7

remove: remove7 remove6 remove5 remove3 remove2 remove1

deploy1:
	cd $(servicedir1); $(deploycmd)

deploy2:
	cd $(servicedir2); $(deploycmd)

deploy3:
	cd $(servicedir3); $(deploycmd)

deploy5:
	cd $(servicedir5); $(deploycmd)

deploy6:
	cd $(servicedir6); $(deploycmd)

deploy7:
	cd $(servicedir7); $(deploycmd)

remove7:
	cd $(servicedir7); $(removecmd)

remove6:
	cd $(servicedir6); $(removecmd)

remove5:
	cd $(servicedir5); $(removecmd)

remove3:
	cd $(servicedir3); $(removecmd)

remove2:
	cd $(servicedir2); $(removecmd)

remove1:
	cd $(servicedir1); $(removecmd)