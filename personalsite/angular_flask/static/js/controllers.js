'use strict';

/* Controllers */

function IndexController($scope) {
	
}

function AboutController($scope) {
	
}

function ProjectGridController($scope, Project) {
	var projectsQuery = Project.ListProjects({}, function(projects) {
		$scope.projects = projects.objects;
	});
}

function ProjectDetailController($scope, $routeParams, Project) {
	var projectQuery = Project.GetProject({ id: $routeParams.projectId }, function(project) {
		$scope.project = project;
	});
}
