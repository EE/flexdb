var app = angular.module("flexdb", []);
var choosenApp;

app.config(function ($interpolateProvider, $httpProvider) {
    $interpolateProvider.startSymbol('[[');
    $interpolateProvider.endSymbol(']]');
    $httpProvider.defaults.xsrfCookieName = 'csrftoken';
    $httpProvider.defaults.xsrfHeaderName = 'X-CSRFToken';
});

app.directive("useredit", function () {
    return {
        restrict: "AEC",
        templateUrl: "/accounts/useredit/",
        transclude: true
    }
});

function overallAppControler($scope, $http, $element, $compile) {
    $scope.apps = {};
    $scope.data = {};
    $scope.user_URL = "";
    $scope.logged = false;
    $scope.applist = true;


    $scope.ajaxDone = function (data) {
        if (data.username != null) {
            $scope.data.username = data.username;
        }
        if (data.first_name != null) {
            $scope.data.first_name = data.first_name;
        }
        if (data.last_name != null) {
            $scope.data.last_name = data.last_name;
        }
        if (data.email != null) {
            $scope.data.email = data.email;
        }
    }


    function loadUserData() {
        $http({
            method: 'GET',
            url: '/accounts/users/'
        }).success(function (data) {
                $scope.ajaxDone(data[0]);
                if (data[0].url != null) {
                    $scope.user_URL = data[0].url;
                    $scope.logged = true;
                }
            })
    }

    $scope.appClick = function (appName) {
        var newElement = $compile("<"+appName+">"+"</"+appName+">")($scope);
        choosenApp(newElement);
        $scope.applist = false;
    }

    $scope.goToAppsList = function () {
        choosenApp(null);
        $scope.applist = true;
    }

    loadUserData();
}

function mainAppControler($scope, $http, $element, $compile) {
    choosenApp = function (el) {
        $element.children(0).remove();
        if(el != null) {
            $element.append(el);
        }
    }
}

function tableControll($scope, $http) {

    $scope.changeUserData = function () {
        $http({
            method: 'PUT',
            url: $scope.user_URL,
            data: angular.toJson($scope.data)
        }).success(function (data) {
                $scope.ajaxDone(data)
            });
    }
}
