'use strict';

/* Controllers */

function IndexController($scope) {
	
}

function AboutController($scope) {
	
}

function ProjectGridController($scope, Post) {
	var projectsQuery = Project.get({}, function(projects) {
		$scope.projects = projects.objects;
	});
}

function ProjectDetailController($scope, $routeParams, Project) {
	var projectQuery = Project.get({ projectId: $routeParams.projectId }, function(project) {
		$scope.project = project;
	});
}
