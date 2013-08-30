app.directive("customUser", function () {
    return {
        restrict: "E",
        templateUrl: "accounts/useredit/",
        transclude: true
    }
});
