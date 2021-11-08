# OrderRequest


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**candidate** | [**MercuryCandidate**](MercuryCandidate.md) |  | 
**assessment_id** | **str** | One component of the uniqueness and idempotency criteria. Must be one of the &#x60;assessment.id&#x60; values from &#x60;Get Assessment Configurations&#x60; | 
**send_email** | **bool** | If true, pymetrics will send an invitation email to the candidate | [optional] [default to False]
**application_id** | **str** | One component of the uniqueness and idempotency criteria. This should relate to your system&#39;s job application ID | 
**requisition_id** | **str** | This will be returned in future API responses | [optional] 
**requisition_title** | **str** | This can be used in email templates if pymetricswill be sending candidates invitation emails. This will be returned in future API responses | [optional] 
**metadata** | **object** | List of key-value pairs that will returned in future API responses | [optional] 
**candidate_redirect_url** | **str** | A URL that redirects candidates back to their respective ATS | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


