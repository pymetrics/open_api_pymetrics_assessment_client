# MercuryAssessmentOrder


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | 
**invite_link** | **str** |  | 
**status** | [**PontemOrderStatuses**](PontemOrderStatuses.md) |  | 
**create_date** | **datetime** |  | 
**candidate** | [**MercuryCandidate**](MercuryCandidate.md) |  | 
**assessment_id** | **str** | Deprecated. Will be removed in a future version. Use assessment object instead | 
**assessment** | [**MercuryAssessment**](MercuryAssessment.md) |  | 
**application_id** | **str** |  | 
**ats_type** | [**AtsType**](AtsType.md) |  | 
**requisition_id** | **str** |  | [optional] 
**requisition_title** | **str** |  | [optional] 
**metadata** | **object** |  | [optional] 
**recruiter_report** | **str** |  | [optional] 
**results** | [**list[MercuryResult]**](MercuryResult.md) |  | [optional] 
**reports** | [**list[MercuryReport]**](MercuryReport.md) |  | [optional] 
**candidate_redirect_url** | **str** |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


