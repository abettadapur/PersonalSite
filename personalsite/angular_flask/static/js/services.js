'use strict';

angular.module('angularFlaskServices', ['ngResource'])
	.factory('Project', function($resource) {
		return $resource('/api/project/', {}, {
			ListProjects: {
				method: 'GET',
				params: {},
				isArray: false
			},
			GetProject: {
				method: 'GET',
				url: '/api/project/:id',
				params: {},
				isArray: false
			}
		});
	})
;



