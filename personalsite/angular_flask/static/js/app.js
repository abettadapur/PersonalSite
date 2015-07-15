'use strict';

angular.module('personalsite',  ['personalsite.home', 'angularFlaskServices', 'ngNewRouter'])
	//.config(componentLoaderConfig)
    .controller("AppController", ['$router', AppController]);

function AppController ($router) {
	console.log("AppController Called");
    $router.config([
        {path: '/', component:'home'}
    ]);
}

function componentLoaderConfig($componentLoaderProivder)
{
	$componentLoaderProivder.setTemplateMapping(function(name) {
		return './static/components/'+name+"/"+name+".html";
	});
}

	/*.config(['$routeProvider', '$locationProvider',
		function($routeProvider, $locationProvider) {
		$routeProvider
		.when('/', {
			templateUrl: 'static/partials/landing.html',
			controller: IndexController
		})
		.when('/about', {
			templateUrl: 'static/partials/about.html',
			controller: AboutController
		})
		.when('/projects', {
			templateUrl: 'static/partials/project-grid.html',
			controller: ProjectGridController
		})
		.when('/projects/:projectId', {
			templateUrl: '/static/partials/project-detail.html',
			controller: ProjectDetailController
		}).when('/contact', {
			templateUrl: 'static/partials/contact.html',
			controller: AboutController
		})
		.otherwise({
			redirectTo: '/'
		})
		;

		$locationProvider.html5Mode(true);
	}])*/

