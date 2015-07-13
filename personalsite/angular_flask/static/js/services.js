'use strict';

angular.module('angularFlaskServices', ['ngResource'])
	.factory('Project', function($resource) {
		return $resource('/api/projects/:projectId', {}, {
			query: {
				method: 'GET',
				params: { projectId: '' },
				isArray: true
			}
		});
	})
;



