# -*- coding: utf-8 -*-

from __future__ import unicode_literals

from expects import expect
from .._helpers import MyList, stub_validator

from booby import validators, errors


class TestList(object):
    def test_should_pass_if_value_is_a_list(self):
        self.validator(['foo', 'bar'])

    def test_should_pass_if_value_is_a_mutable_sequence(self):
        self.validator(MyList('foo', 'bar'))

    def test_should_fail_if_value_is_not_a_list(self):
        expect(lambda: self.validator(object())).to.raise_error(
            errors.ValidationError, 'should be a list')

    def test_should_fail_if_value_is_none(self):
        expect(lambda: self.validator(None)).to.raise_error(
            errors.ValidationError, 'should be a list')

    def test_should_fail_if_inner_validator_fails(self):
        def inner_validator(value):
            if value == 'bar':
                raise errors.ValidationError('invalid')

        self.validator = validators.List(stub_validator, inner_validator)

        expect(lambda: self.validator(['foo', 'bar'])).to.raise_error(
            errors.ValidationError, 'invalid')

    def test_when_described_then_type_is_array(self):
        expect(self.validator.describe()).to.have.key('type', 'array')

    def setup(self):
        self.validator = validators.List()
