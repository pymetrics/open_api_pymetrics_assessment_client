# coding: utf-8

"""
    pymetrics API

    ### This is pymetrics's public API. The API can be used to get information on candidates as part of a job application workflow, or for employee career pathing and development. The typical use case for this is to support an externally initiated assessment for a candidate job application. This is often done \"inline\" with the candidate's application, or asynchronously after the candidate submits their application. This data can then be used for career pathing and employee development in subsequent stages.  The expected sequence of API calls is: * `Generate OAuth Token` with the OAuth Client ID and Secret you've been provided * `Get Assessment Configurations` to determine which configured assessment templates are available * `Create Assessment Order` for a selected Assessment and candidate job application * `Get Assessment Order` to receive the recommendation results and reports, once they are available  # noqa: E501

    The version of the OpenAPI document: 2.2.0
    Generated by: https://openapi-generator.tech
"""


try:
    from inspect import getfullargspec
except ImportError:
    from inspect import getargspec as getfullargspec
import pprint
import re  # noqa: F401
import six

from openapi_client.configuration import Configuration


class OrderRequest(object):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    openapi_types = {
        'candidate': 'MercuryCandidate',
        'assessment_id': 'str',
        'send_email': 'bool',
        'application_id': 'str',
        'requisition_id': 'str',
        'requisition_title': 'str',
        'metadata': 'object',
        'candidate_redirect_url': 'str'
    }

    attribute_map = {
        'candidate': 'candidate',
        'assessment_id': 'assessment_id',
        'send_email': 'send_email',
        'application_id': 'application_id',
        'requisition_id': 'requisition_id',
        'requisition_title': 'requisition_title',
        'metadata': 'metadata',
        'candidate_redirect_url': 'candidate_redirect_url'
    }

    def __init__(self, candidate=None, assessment_id=None, send_email=False, application_id=None, requisition_id=None, requisition_title=None, metadata=None, candidate_redirect_url=None, local_vars_configuration=None):  # noqa: E501
        """OrderRequest - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration.get_default_copy()
        self.local_vars_configuration = local_vars_configuration

        self._candidate = None
        self._assessment_id = None
        self._send_email = None
        self._application_id = None
        self._requisition_id = None
        self._requisition_title = None
        self._metadata = None
        self._candidate_redirect_url = None
        self.discriminator = None

        self.candidate = candidate
        self.assessment_id = assessment_id
        if send_email is not None:
            self.send_email = send_email
        self.application_id = application_id
        if requisition_id is not None:
            self.requisition_id = requisition_id
        if requisition_title is not None:
            self.requisition_title = requisition_title
        if metadata is not None:
            self.metadata = metadata
        if candidate_redirect_url is not None:
            self.candidate_redirect_url = candidate_redirect_url

    @property
    def candidate(self):
        """Gets the candidate of this OrderRequest.  # noqa: E501


        :return: The candidate of this OrderRequest.  # noqa: E501
        :rtype: MercuryCandidate
        """
        return self._candidate

    @candidate.setter
    def candidate(self, candidate):
        """Sets the candidate of this OrderRequest.


        :param candidate: The candidate of this OrderRequest.  # noqa: E501
        :type candidate: MercuryCandidate
        """
        if self.local_vars_configuration.client_side_validation and candidate is None:  # noqa: E501
            raise ValueError("Invalid value for `candidate`, must not be `None`")  # noqa: E501

        self._candidate = candidate

    @property
    def assessment_id(self):
        """Gets the assessment_id of this OrderRequest.  # noqa: E501

        One component of the uniqueness and idempotency criteria. Must be one of the `assessment.id` values from `Get Assessment Configurations`  # noqa: E501

        :return: The assessment_id of this OrderRequest.  # noqa: E501
        :rtype: str
        """
        return self._assessment_id

    @assessment_id.setter
    def assessment_id(self, assessment_id):
        """Sets the assessment_id of this OrderRequest.

        One component of the uniqueness and idempotency criteria. Must be one of the `assessment.id` values from `Get Assessment Configurations`  # noqa: E501

        :param assessment_id: The assessment_id of this OrderRequest.  # noqa: E501
        :type assessment_id: str
        """
        if self.local_vars_configuration.client_side_validation and assessment_id is None:  # noqa: E501
            raise ValueError("Invalid value for `assessment_id`, must not be `None`")  # noqa: E501

        self._assessment_id = assessment_id

    @property
    def send_email(self):
        """Gets the send_email of this OrderRequest.  # noqa: E501

        If true, pymetrics will send an invitation email to the candidate  # noqa: E501

        :return: The send_email of this OrderRequest.  # noqa: E501
        :rtype: bool
        """
        return self._send_email

    @send_email.setter
    def send_email(self, send_email):
        """Sets the send_email of this OrderRequest.

        If true, pymetrics will send an invitation email to the candidate  # noqa: E501

        :param send_email: The send_email of this OrderRequest.  # noqa: E501
        :type send_email: bool
        """

        self._send_email = send_email

    @property
    def application_id(self):
        """Gets the application_id of this OrderRequest.  # noqa: E501

        One component of the uniqueness and idempotency criteria. This should relate to your system's job application ID  # noqa: E501

        :return: The application_id of this OrderRequest.  # noqa: E501
        :rtype: str
        """
        return self._application_id

    @application_id.setter
    def application_id(self, application_id):
        """Sets the application_id of this OrderRequest.

        One component of the uniqueness and idempotency criteria. This should relate to your system's job application ID  # noqa: E501

        :param application_id: The application_id of this OrderRequest.  # noqa: E501
        :type application_id: str
        """
        if self.local_vars_configuration.client_side_validation and application_id is None:  # noqa: E501
            raise ValueError("Invalid value for `application_id`, must not be `None`")  # noqa: E501

        self._application_id = application_id

    @property
    def requisition_id(self):
        """Gets the requisition_id of this OrderRequest.  # noqa: E501

        This will be returned in future API responses  # noqa: E501

        :return: The requisition_id of this OrderRequest.  # noqa: E501
        :rtype: str
        """
        return self._requisition_id

    @requisition_id.setter
    def requisition_id(self, requisition_id):
        """Sets the requisition_id of this OrderRequest.

        This will be returned in future API responses  # noqa: E501

        :param requisition_id: The requisition_id of this OrderRequest.  # noqa: E501
        :type requisition_id: str
        """

        self._requisition_id = requisition_id

    @property
    def requisition_title(self):
        """Gets the requisition_title of this OrderRequest.  # noqa: E501

        This can be used in email templates if pymetricswill be sending candidates invitation emails. This will be returned in future API responses  # noqa: E501

        :return: The requisition_title of this OrderRequest.  # noqa: E501
        :rtype: str
        """
        return self._requisition_title

    @requisition_title.setter
    def requisition_title(self, requisition_title):
        """Sets the requisition_title of this OrderRequest.

        This can be used in email templates if pymetricswill be sending candidates invitation emails. This will be returned in future API responses  # noqa: E501

        :param requisition_title: The requisition_title of this OrderRequest.  # noqa: E501
        :type requisition_title: str
        """

        self._requisition_title = requisition_title

    @property
    def metadata(self):
        """Gets the metadata of this OrderRequest.  # noqa: E501

        List of key-value pairs that will returned in future API responses  # noqa: E501

        :return: The metadata of this OrderRequest.  # noqa: E501
        :rtype: object
        """
        return self._metadata

    @metadata.setter
    def metadata(self, metadata):
        """Sets the metadata of this OrderRequest.

        List of key-value pairs that will returned in future API responses  # noqa: E501

        :param metadata: The metadata of this OrderRequest.  # noqa: E501
        :type metadata: object
        """

        self._metadata = metadata

    @property
    def candidate_redirect_url(self):
        """Gets the candidate_redirect_url of this OrderRequest.  # noqa: E501

        A URL that redirects candidates back to their respective ATS  # noqa: E501

        :return: The candidate_redirect_url of this OrderRequest.  # noqa: E501
        :rtype: str
        """
        return self._candidate_redirect_url

    @candidate_redirect_url.setter
    def candidate_redirect_url(self, candidate_redirect_url):
        """Sets the candidate_redirect_url of this OrderRequest.

        A URL that redirects candidates back to their respective ATS  # noqa: E501

        :param candidate_redirect_url: The candidate_redirect_url of this OrderRequest.  # noqa: E501
        :type candidate_redirect_url: str
        """
        if (self.local_vars_configuration.client_side_validation and
                candidate_redirect_url is not None and len(candidate_redirect_url) > 65536):
            raise ValueError("Invalid value for `candidate_redirect_url`, length must be less than or equal to `65536`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                candidate_redirect_url is not None and len(candidate_redirect_url) < 1):
            raise ValueError("Invalid value for `candidate_redirect_url`, length must be greater than or equal to `1`")  # noqa: E501

        self._candidate_redirect_url = candidate_redirect_url

    def to_dict(self, serialize=False):
        """Returns the model properties as a dict"""
        result = {}

        def convert(x):
            if hasattr(x, "to_dict"):
                args = getfullargspec(x.to_dict).args
                if len(args) == 1:
                    return x.to_dict()
                else:
                    return x.to_dict(serialize)
            else:
                return x

        for attr, _ in six.iteritems(self.openapi_types):
            value = getattr(self, attr)
            attr = self.attribute_map.get(attr, attr) if serialize else attr
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: convert(x),
                    value
                ))
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], convert(item[1])),
                    value.items()
                ))
            else:
                result[attr] = convert(value)

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, OrderRequest):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, OrderRequest):
            return True

        return self.to_dict() != other.to_dict()
